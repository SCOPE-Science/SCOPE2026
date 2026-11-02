# A binary-weight classification of isolated gaps in Proth numerical semigroups

## Finding

For every integer \(m\ge3\), consider the numerical semigroup
\[
S_m=\langle 2^i(m-1)+1:i\ge0\rangle.
\]
An *isolated gap* is a positive integer outside the semigroup whose immediate predecessor and successor both belong to the semigroup. Write \(I(S_m)\) for the set of isolated gaps, \(F(S_m)\) for the largest gap, and \(L(t)\) for the minimum number of positive Mersenne coins \(2^i-1\), \(i\ge1\), summing to \(t\), with \(L(0)=0\). Then the complete isolated-gap classification is
\[
I(S_m)=\begin{cases}
\{F(S_m)-m,F(S_m)\},&L(m-1)=L(m-2)+1,\\
\varnothing,&L(m-1)=L(m-2)-1.
\end{cases}
\]
In the first case,
\[
F(S_m)=(m-1)^2+m\bigl(L(m-1)-1\bigr).
\]
In particular, there are **never exactly one or more than two** isolated gaps in this entire infinite family.

For the Proth semigroup \(P_k(n)=S_{k2^n+1}\), where \(n\ge3\) and \(k\) is odd with \(1\le k<2^n\), put \(s=s_2(k)\), the number of ones in the binary expansion of \(k\), and
\[
\mathcal A=\{2j+1-s_2(j):j\in\mathbb Z_{\ge0}\}.
\]
Then the criterion becomes **purely a binary-weight criterion**:
\[
I(P_k(n))=\begin{cases}
\{F(P_k(n))-(k2^n+1),F(P_k(n))\},&s\in\mathcal A,\\
\varnothing,&s\notin\mathcal A.
\end{cases}
\]
Consequently \(P_k(n)\) is a perfect numerical semigroup (has no isolated gaps) exactly when \(s_2(k)\notin\mathcal A\), independently of \(n\). In the nonperfect case the displayed Frobenius number is explicitly
\[
F(P_k(n))=(k2^n)^2+(k2^n+1)(2j_s-1),\quad
j_s=\min\{j\ge1:2j-s_2(j)\ge s\}.
\]
For example, \(k=3\) (binary weight two) gives exactly two isolated gaps for every admissible \(n\), whereas \(k=7\) (binary weight three) gives none.

## Assumptions and scope

The semigroups use nonnegative integer sums, and the generator with \(i=0\) is \(m\). Since \(\gcd(m,2m-1)=1\), each \(S_m\) is a numerical semigroup. Integers \(m\) may be even or odd. The Proth specialization requires \(n\ge3\), odd \(k\), and \(1\le k<2^n\). The binary weight \(s_2(0)=0\). In the empty-gap case no formula for the Frobenius number is asserted by the main display.

## Proof

**1. Exact Apéry minima.** Put \(d_i=2^i-1\) for \(i\ge1\). Then
\[
2^i(m-1)+1=(m-1)d_i+m.
\]
A sum using \(\ell\) nonzero-index generators with total Mersenne-coin weight \(t\) has value \((m-1)t+m\ell\), with residue \(-t\pmod m\). For each residue \(1\le r<m\), the least positive allowable \(t\) is \(t_0=m-r\). Using \(t_0\) copies of \(d_1=1\) gives a candidate of value at most \((m-1)t_0+mt_0\). Any larger allowable weight \(t\ge t_0+m\) yields a value at least \((m-1)(t_0+m)+m\), which is strictly larger since \(t_0\le m-1\). Therefore the Apéry minima are exactly
\[
w_0=0,\qquad w_r=(m-1)(m-r)+mL(m-r)\quad(1\le r<m).
\]
The presence of the generator \(m\) does not affect these minima.

**2. One-step coin-length law.** Every \(d_i\) is odd, so \(L(t)\equiv t\pmod2\). Appending \(d_1=1\) shows \(L(t+1)\le L(t)+1\). Conversely, in an optimal decomposition of \(t+1\), either delete a coin \(d_1\), or replace some coin \(d_i\), \(i\ge2\), by two copies of \(d_{i-1}\), since \(d_i-1=2d_{i-1}\). Either operation produces a representation of \(t\) of length at most \(L(t+1)+1\). Thus
\[
L(t+1)-L(t)\in\{-1,1\}\qquad(t\ge0).
\]
For \(2\le r<m\), the Apéry differences satisfy
\[
w_r-w_{r-1}=-(m-1)+m\bigl(L(m-r)-L(m-r+1)\bigr)\le1.
\]
Every gap of residue \(r\ge2\) is below \(w_r\), hence its predecessor is below \(w_{r-1}\) and is also a gap. A gap in residue zero is impossible. Therefore an isolated gap must have residue one.

**3. Exactly zero or two isolated gaps.** The residue-one gaps have the form \(g=w_1-jm\), \(j\ge1\), as long as \(g>0\). Their predecessors are nonnegative multiples of \(m\), hence are in the semigroup. Their successors lie in the semigroup precisely when
\[
w_1-jm+1\ge w_2.
\]
The Apéry formula gives
\[
w_1-w_2+1=m\bigl(1+L(m-1)-L(m-2)\bigr).
\]
By the one-step law, this is either zero or \(2m\); hence no \(j\) or exactly \(j=1,2\) qualifies. In the latter case both candidates are positive, since \(L(m-1)\ge2\). Moreover, defining \(f(t)=(m-1)t+mL(t)\), each \(f(t+1)-f(t)\ge-1\), while the last step from \(m-2\) to \(m-1\) equals \(2m-1\). This last increase exceeds any possible preceding accumulated decrease, so \(w_1=f(m-1)\) is the largest Apéry element. Hence \(F(S_m)=w_1-m\), proving the first assertion and the displayed Frobenius formula.

**4. Binary-weight reduction.** An expression of \(t\) as exactly \(\ell\) positive Mersenne coins is equivalent to an expression of \((t+\ell)/2\) as exactly \(\ell\) positive powers of two. An integer \(u\ge1\) is a sum of exactly \(\ell\) powers of two if and only if \(s_2(u)\le\ell\le u\): start with its binary expansion, and repeatedly split a power of two until the desired count is reached. Therefore
\[
L(t)=\min\{\ell\ge0:\ell\equiv t\pmod2,\quad s_2((t+\ell)/2)\le\ell\le(t+\ell)/2\}.
\]
Here \(t=k2^n\), \(1\le s=s_2(k)\le n\). A trial \(\ell=2s\) is feasible for \(t\), and \(\ell=2s-1\) is feasible for \(t-1\). Since \(2n<2^n\) for \(n\ge3\), all minimizing parameters \(j\) are strictly below \(2^{n-1}\). Consequently no binary carry occurs in
\[
\frac{k2^n+2j}{2}=k2^{n-1}+j
\]
or its odd counterpart. Defining
\[
j_s=\min\{j\ge1: s+s_2(j)\le2j\},\quad
h_s=\min\{j\ge0:s+s_2(j)\le2j+1\},
\]
gives the exact lengths
\[
L(k2^n)=2j_s,\qquad L(k2^n-1)=2h_s+1.
\]
The sequence \(a(j)=2j-s_2(j)\) increases strictly with \(j\), because \(s_2(j+1)-s_2(j)\le1\). Hence \(h_s=j_s-1\) precisely when \(s=a(j_s-1)+1\), which is equivalent to \(s\in\mathcal A\); otherwise \(h_s=j_s\). Thus \(L(k2^n)-L(k2^n-1)\) equals \(+1\) exactly when \(s\in\mathcal A\), and equals \(-1\) otherwise. Apply Steps 2–3 with \(m=k2^n+1\) to finish.

## Verification

The accompanying `verify.py` performs independent shortest-path computations in the residue graph to recover Apéry minima; it uses dynamic programming over coin weights to check the derived closed formula and enumerates isolated gaps from those Apéry representatives. It checks all \(199\) values \(3\le m\le201\), all \(60\) admissible Proth parameter pairs with \(3\le n\le6\), eight additional larger pairs, and binary-weight thresholds \(1\le s\le128\). The execution returned `VERIFY_OK general_m=199 proth_pairs=68 popcount_thresholds=128`. These are finite consistency checks; the proof above establishes the unrestricted statements.

## Relationship to prior work

Srivastava and Thakkar introduced Proth numerical semigroups and developed Frobenius/Apéry results, with their explicit central theorems focusing on \(k=2^r+1\). They do not derive the above isolated-gap criterion or the all-\(k\) binary-weight classification. Smith established general links between isolated gaps and Apéry elements, and Singh and Ram provided an exact treatment of embedding-dimension-two semigroups. Moreno-Frías and Rosales studied perfect semigroups at fixed Frobenius number via covarieties. The present statement specializes those broader ideas to a distinct infinite generator family and supplies an explicit binary criterion; existing general algorithms alone do not imply the displayed uniform formulas without further analysis.

## Limitations

The result concerns isolated gaps, not the entire gap set or pseudo-Frobenius set. It does not give a closed Frobenius formula for the perfect cases. An equivalent identity could exist in unindexed literature; bibliographic priority is not independently certified. Smith's publisher-hosted full text was not available for material inspection, so the comparison with that paper uses its published abstract and the independently inspected related open-access articles. The finite checks cannot independently certify the infinite proof.

## References

1. P. Srivastava and D. Thakkar, *The Frobenius Problem for the Proth Numbers*, arXiv:2311.12462v1 (21 November 2023), https://arxiv.org/abs/2311.12462.
2. H. J. Smith, *On isolated gaps in numerical semigroups*, Turkish Journal of Mathematics 46 (2022), 123–129, doi:10.3906/mat-2107-54.
3. S. N. Singh and R. K. Ram, *On Isolated Gaps of Numerical Semigroups of embedding dimension two*, arXiv:2406.09848v1 (14 June 2024), https://arxiv.org/abs/2406.09848.
4. M. Á. Moreno-Frías and J. C. Rosales, *The covariety of perfect numerical semigroups with fixed Frobenius number*, arXiv:2305.14967v1 (24 May 2023), https://arxiv.org/abs/2305.14967.
