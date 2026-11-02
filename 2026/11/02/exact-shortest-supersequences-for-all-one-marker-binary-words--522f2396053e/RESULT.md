# Exact shortest supersequences for all one-marker binary words

## Finding

For each integer \(k\ge 1\), let \(\mathcal T_k=\{0^i1 0^{k-1-i}:0\le i<k\}\), where the spaces in the displayed pattern are concatenation. A binary word covers \(\mathcal T_k\) when every member occurs as a scattered subsequence. If its number of ones is prescribed to be \(r\ge1\), the minimum possible host length is
\[
L_k(r)=k-2+r+\left\lceil\frac{k}{r}\right\rceil.
\]
Without prescribing \(r\), the exact minimum is
\[
L_k=k-2+\left\lceil2\sqrt{k}\right\rceil.
\]
In addition to these sharp lengths, all covering hosts have the interval characterization below. In particular, put \(s=\lceil k/r\rceil\) and \(\delta=rs-k\). The number \(C_{k,r}\) of optimal-length hosts containing exactly \(r\) ones is
\[
C_{k,r}=[y^\delta](1+y+\cdots+y^{s-1})^2(1+y+\cdots+y^s)^{r-1}.
\]
Consequently the total number of shortest covering words is
\[
H_k=\sum_{\substack{r\ge1\\r+\lceil k/r\rceil=\lceil2\sqrt{k}\rceil}} C_{k,r}.
\]
For every perfect square \(k=t^2\), this shortest host is **unique** and equals
\[
0^{t-1}1(0^t1)^{t-1}0^{t-1}.
\]
The word above includes the case \(t=1\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). A scattered subsequence preserves left-to-right order, with gaps allowed; it is not required to be contiguous. The target set contains all \(k\) words of length \(k\) having exactly one occurrence of \(1\). The host may contain any number of zeros and ones, except when its number \(r\) of ones is explicitly fixed. All parameters are positive integers. Distinct hosts are distinct binary strings, not equivalence classes under reversal or complementation. Throughout, \([y^d]F(y)\) denotes the coefficient of \(y^d\) in \(F\).

For a host with \(z\) zeros and \(r\) ones, let \(0\le x_1\le\cdots\le x_r\le z\) be the cumulative numbers of zeros preceding its successive ones. Every host has a unique such vector. If \(z\ge k-1\), set \(s=z-k+2\). Then the following are equivalent: the host covers \(\mathcal T_k\); and
\[
x_1\le s-1,\qquad x_r\ge k-1,\qquad
x_{j+1}-x_j\le s\quad (1\le j<r).
\]
The monotonicity and endpoint bounds on the \(x_j\)'s remain part of the definitions. This criterion also covers \(k=1\). If \(z<k-1\) or \(r=0\), coverage is impossible.

## Proof

**1. One marker supplies an interval of target positions.** Fix \(k\ge1\) and a host with \(z\) zeros and \(r\) ones. For a chosen host one preceded by \(x\) zeros, the target \(0^i1 0^{k-1-i}\) embeds through this occurrence precisely when \(i\le x\) and \(k-1-i\le z-x\). Equivalently, the integer \(i\) belongs to
\[
I(x)=[x-s+1,x]\cap[0,k-1],\quad s=z-k+2.
\]
Necessarily \(z\ge k-1\). With \(s\ge1\), each interval has at most \(s\) integer positions. Since the \(x_j\)'s are nondecreasing, their union equals all integers in \([0,k-1]\) if and only if the first interval contains zero, the last contains \(k-1\), and no two consecutive intervals leave an integer gap. These three conditions are exactly the stated inequalities. No unproved algorithmic assertion is needed.

**2. Sharp fixed-marker length.** Each of the \(r\) intervals contains at most \(s\) target positions, so coverage implies \(rs\ge k\), hence \(s\ge\lceil k/r\rceil\). As \(z=k-2+s\), every covering host has length at least \(k-2+r+\lceil k/r\rceil\). For sufficiency set \(s=\lceil k/r\rceil\), \(z=k-2+s\), and choose
\[
x_j=\min\{js-1,k-1\}\qquad(1\le j\le r).
\]
These integers are nondecreasing, lie between zero and \(z\), have successive differences at most \(s\), and satisfy the first and last endpoint conditions because \(rs\ge k\). Placing the ones at these cumulative-zero positions constructs an actual host of the asserted length, proving the fixed-marker formula.

**3. Global sharp length.** For positive integers \(r,s\) with \(rs\ge k\), the arithmetic-geometric mean inequality yields \(r+s\ge2\sqrt{rs}\ge2\sqrt{k}\), so the integer sum satisfies \(r+s\ge\lceil2\sqrt{k}\rceil\). Conversely let \(c=\lceil2\sqrt{k}\rceil\), \(r=\lfloor c/2\rfloor\), and \(s=\lceil c/2\rceil\). The product \(rs=\lfloor c^2/4\rfloor\) is at least the integer \(k\), since \(c^2/4\ge k\). Using the construction of Step 2, these values attain total length \(k-2+c\). (For \(k=1\) the choice is \(r=s=1\).)

**4. Exact enumeration for a fixed number of ones.** At the fixed-marker optimum \(s=\lceil k/r\rceil\), define the nonnegative slack variables
\[
\alpha=s-1-x_1,\qquad\beta=x_r-(k-1),\qquad
\gamma_j=s-(x_{j+1}-x_j),\quad1\le j<r.
\]
The coverage criterion implies \(0\le\alpha,\beta\le s-1\) and \(0\le\gamma_j\le s\). Direct telescoping gives
\[
\alpha+\beta+\sum_{j=1}^{r-1}\gamma_j=rs-k=\delta.
\]
Conversely any nonnegative variables within these bounds and with this sum determine \(x_1=s-1-\alpha\), then determine all successive \(x_{j+1}=x_j+s-\gamma_j\). Their last value is \(k-1+\beta\), which is at most \(z=k-2+s\). They therefore determine exactly one host, and every such host is obtained. Counting bounded compositions yields the stated coefficient formula. Different values of \(r\) give different binary hosts, proving the sum for \(H_k\).

**5. Rigidity at square lengths.** If \(k=t^2\) and a host is globally shortest, then \(r+s\le2t\) and \(rs\ge t^2\). Equality in arithmetic-geometric mean forces \(r=s=t\); the slack sum is zero. Every slack is therefore zero, so the unique zero-prefix vector is \(x_j=jt-1\). Its host is exactly \(0^{t-1}1(0^t1)^{t-1}0^{t-1}\). This also proves its uniqueness.

## Verification

A standalone standard-library checker is included as `verify_onehot.py`. It enumerates every binary host through the theoretically minimal length for each \(1\le k\le11\), compares literal scattered-subsequence coverage with the interval criterion, excludes every shorter host, and compares counts of shortest hosts to the coefficient formula. For \(1\le k\le8\), it also counts optimal hosts separately at fixed numbers of ones, comparing with polynomial coefficients. Large-parameter tests check the integer minimization identity and constructive witnesses for \(1\le k\le2000\); these are arithmetic/computational spot checks and do not replace the universal proof above.

Running `python3 verify_onehot.py` in the extracted package yields:

```
VERIFY_OK checked_hosts=227017 k_global=1..11 optimal_counts={1: 1, 2: 2, 3: 5, 4: 1, 5: 7, 6: 2, 7: 18, 8: 6, 9: 1, 10: 27, 11: 9} fixed_marker_profiles=52 integer_witness_k=1..2000
```

## Relationship to prior work

Scattered-subsequence universality normally requires **every** length-\(k\) word over the entire alphabet (Barker et al.; Adamson). Nearly universal words constrain the number of missing length-\(k\) words (Fleischmann et al.). The present target language instead contains exactly those length-\(k\) binary words having one occurrence of \(1\). It is neither the full length-\(k\) spectrum nor a bounded-deficiency spectrum. In particular, the full-universality algorithms and enumerations do not by themselves imply the optimal lengths, precise fixed-marker optimizer count, or square-length rigidity here. A survey of the cited full texts and related results did not locate these exact formulas; absence from a search is not a proof of historical novelty.

## Limitations

The theorem treats only the one-marker target language and says nothing directly about languages with two or more required ones. No optimality assertion for such extensions is made. The counts treat binary words as labeled strings; quotients by reversal or other symmetries are not counted. All mathematical conclusions follow from the proof, not from finite enumeration. Although no equivalent statement was found in the checked sources, equivalent specializations of broader shortest-common-supersequence results may exist.

## References

1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, and D. Nowotka, *Scattered Factor-Universality of Words*, publicly available 2020-03-10, https://arxiv.org/abs/2003.04629 .
2. P. Fleischmann, L. Haschke, A. Huch, A. Mayrock, and D. Nowotka, *m-Nearly k-Universal Words — Investigating Simon Congruence*, publicly available 2022-02-16, https://arxiv.org/abs/2202.07981 .
3. D. Adamson, *Ranking and Unranking k-subsequence universal words*, publicly available 2023-04-10, https://arxiv.org/abs/2304.04583 .
