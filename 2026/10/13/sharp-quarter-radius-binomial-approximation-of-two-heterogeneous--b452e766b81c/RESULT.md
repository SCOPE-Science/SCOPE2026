# Sharp quarter-radius binomial approximation of two heterogeneous Bernoulli trials

## Finding

Let \(B_p\) and \(B_q\) be independent Bernoulli random variables with arbitrary \(p,q\in[0,1]\), and put \(S=B_p+B_q\). Let
\[
\mathcal B=\{\operatorname{Bin}(m,r):m\in\{1,2,3,\ldots\},\ 0\le r\le1\},
\qquad
\delta(p,q)=\inf_{Q\in\mathcal B}d_{\mathrm{TV}}(\mathcal L(S),Q).
\]
Here \(d_{\mathrm{TV}}(P,Q)=\sup_{A\subseteq\mathbb Z_{\ge0}}|P(A)-Q(A)|\), equal to half the sum of absolute point-mass differences.

**Theorem.** The unrestricted-binomial approximation radius of the entire two-trial Poisson-binomial family is exactly
\[
\boxed{\ \sup_{p,q\in[0,1]}\delta(p,q)=\frac14\ }.
\]
The only maximizing ordered parameter pairs are \((p,q)=(1,1/4)\) and \((p,q)=(1/4,1)\). Both include a deterministic success; consequently the supremum is sharp but unattained when both parameters are restricted to \((0,1)\).

Moreover, for **each** parameter pair at least one of the following two explicit approximations has total-variation error at most \(1/4\):
\[
\begin{aligned}
Q_1&=\operatorname{Bin}(1,p+q-pq),
&d_{\mathrm{TV}}(\mathcal L(S),Q_1)&=pq,\\
Q_2&=\operatorname{Bin}(2,\sqrt{pq}),
&d_{\mathrm{TV}}(\mathcal L(S),Q_2)&=(\sqrt p-\sqrt q)^2.
\end{aligned}
\]
Thus allowing three or more binomial trials cannot improve the **worst-case** guarantee, although the theorem does not determine the pointwise best binomial approximation for every \((p,q)\).

## Assumptions and scope

The two Bernoulli variables are independent; their success probabilities may differ and may equal zero or one. The approximating binomial may have **any positive integer** number of trials and any success probability in the closed unit interval; no equal-mean or equal-variance constraint is imposed. Distributions are on the nonnegative integers, and total variation includes all singleton and tail events. The result concerns only two source summands, not arbitrary numbers of Bernoulli trials.

## Proof

The exact probability masses of \(S\), at \(0,1,2\) respectively, are
\[
P_0=(1-p)(1-q),\qquad P_1=p+q-2pq,\qquad P_2=pq.
\]

**First explicit approximation.** Set \(r_1=p+q-pq=1-P_0\). The one-trial law \(Q_1=\operatorname{Bin}(1,r_1)\) agrees with \(P\) at zero, has mass \(P_1+P_2\) at one, and has no mass at two. Therefore the signed point-mass difference is \((0,-pq,+pq)\), so
\[
d_{\mathrm{TV}}(P,Q_1)=pq.
\]

**Second explicit approximation.** Set \(r_2=\sqrt{pq}\) and take \(Q_2=\operatorname{Bin}(2,r_2)\). Its mass at two equals \(P_2\). At zero its mass exceeds \(P_0\) by
\[
(1-r_2)^2-(1-p)(1-q)=p+q-2\sqrt{pq}=(\sqrt p-\sqrt q)^2\ge0.
\]
The opposite difference occurs at one, whence
\[
d_{\mathrm{TV}}(P,Q_2)=(\sqrt p-\sqrt q)^2.
\]
These identities hold at all boundary parameter values.

**Universal bound and uniqueness of possible maximizers.** If \(pq<1/4\), the first approximation has error strictly below \(1/4\). Otherwise order the parameters as \(p\ge q\) without loss of generality. From \(pq\ge1/4\) and \(p\le1\), we get \(q\ge1/(4p)\ge1/4\). Hence
\[
0\le\sqrt p-\sqrt q\le1-\frac12=\frac12,
\quad\text{so}\quad
 d_{\mathrm{TV}}(P,Q_2)\le\frac14.
\]
Equality here requires simultaneously \(p=1\) and \(q=1/4\). Thus \(\delta(p,q)\le1/4\) everywhere, and the only parameters at which equality *could* occur are the two asserted ordered pairs.

**Sharpness against every binomial trial count.** At \((p,q)=(1,1/4)\), the law is
\[
P\{0\}=0,\quad P\{1\}=\frac34,\quad P\{2\}=\frac14.
\]
For a one-trial approximation, the event \(\{2\}\) forces total variation at least \(1/4\). For every \(m\ge2\) and \(r\in[0,1]\), a binomial law satisfies
\[
\Pr\{\operatorname{Bin}(m,r)=1\}=mr(1-r)^{m-1}
\le\left(1-\frac1m\right)^{m-1}\le\frac12.
\]
The first inequality follows by differentiating in \(r\) (the maximizer is \(r=1/m\)); the second follows from the binomial theorem applied to \((1+1/(m-1))^{m-1}\ge2\). Hence the event \(\{1\}\) forces total variation at least \(3/4-1/2=1/4\), for **every** \(m\ge2\). Equality \(1/4\) is attained by \(\operatorname{Bin}(1,1)\) and also by \(\operatorname{Bin}(2,1/2)\), as the first two identities show. Thus \(\delta(1,1/4)=1/4\); symmetry gives the other maximizing ordered pair. This completes the global supremum and uniqueness claims.

## Verification

The standalone standard-library script `verify.py` evaluates the two explicit total-variation identities using exact rational arithmetic on finite grids, checks the strict-bound/equality cases accessible on those grids, and checks the extremal lower bound against 50 binomial trial counts and 65 rational success probabilities each. Run with `python3 verify.py`. The observed output was:

```
VERIFY_OK low_rational=655 high_square_rational=174 extremal_tests=3250
```

The verifier is a finite consistency check, **not** an exhaustive proof over real parameters or all trial counts. Those universal quantifiers follow from the analytical argument above.

## Relationship to prior work

Jaramillo and Melbourne (2022, Remark 2.4) explicitly pose the optimization of binomial trial count and success probability for approximation of a Poisson-binomial law in total variation; their Corollary 2.2 gives an inequality for a same-size binomial parameter choice. This theorem instead identifies the sharp **worst-case two-summand radius** when both binomial parameters are unrestricted; it does not solve their entire pointwise parameter-optimization problem.

Roos (2000, §§1–2) derives a Krawtchouk expansion and bounds for approximating a Poisson-binomial sum by a **same-trial-count** binomial with arbitrary success probability. Choi and Xia (2002) study binomials under mean matching, especially a large-mean comparison with Poisson approximation. These statements do not provide the radius over both one-trial and unrestricted-trial approximants or its unique two-coin extremizers. Ehm (1991) concerns a same-size, mean-matched approximation in the available abstract; its complete text was not accessible for a definitive whole-paper exclusion. Tang and Tang's survey (2023) supplies broader background.

## Limitations

The result determines an extremal covering radius and its equality cases, not an explicit formula for \(\delta(p,q)\) for every individual pair, nor the optimal binomial trial count at every pair. It makes no assertion for sums of three or more heterogeneous Bernoulli variables. A fully comprehensive historical priority determination has not been performed; an equivalent earlier formulation might exist, notably in older approximation or discrete probability literature. Numerical grid checks cannot settle originality or infinite quantifiers.

## References

1. A. Jaramillo and J. Melbourne, *Quantitative limit theorems via relative log-concavity*, arXiv:2210.11632v1 (first public version, 2022-10-20), especially Corollary 2.2 and Remark 2.4. https://arxiv.org/pdf/2210.11632
2. B. Roos, *Binomial approximation to the Poisson binomial distribution: The Krawtchouk expansion*, Teoriya Veroyatnostei i ee Primeneniya 45(2) (2000), 328–344; English translation, Theory Probab. Appl. 45 (2001), 258–272. https://www.mathnet.ru/eng/tvp466
3. K. P. Choi and A. Xia, *Approximating the number of successes in independent trials: Binomial versus Poisson*, Ann. Appl. Probab. 12(4) (2002), 1139–1148. https://doi.org/10.1214/aoap/1037125856
4. W. Ehm, *Binomial approximation to the Poisson binomial distribution*, Statistics & Probability Letters 11 (1991), 7–16. https://doi.org/10.1016/0167-7152(91)90170-V
5. W. Tang and F. Tang, *The Poisson binomial distribution—Old & New*, Statistical Science 38(1) (2023), 108–119. https://doi.org/10.1214/22-STS852
