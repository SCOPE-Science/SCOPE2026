# First post-threshold Apéry set for the Pell triple \(P_4(u),P_6(u),P_9(u)\)

## Finding

Let \(u\ge2\) be an integer, and define the Pell polynomials by \(P_0(u)=0\), \(P_1(u)=1\), and \(P_{n+2}(u)=uP_{n+1}(u)+P_n(u)\). Put
\[
 s=u^2+2,\quad p=u^2=s-2,\quad a=P_4(u)=us,\quad b=P_6(u)=u(s^2-1),\quad c=P_9(u).
\]
For an integer \(N\ge0\), let \(d(N)\) count nonnegative triples \((x,y,z)\) with \(ax+by+cz=N\). The \(p\)-Apéry set comprises the least element of \(\{N:d(N)>p\}\) in each class modulo \(a\).

**Theorem.** For every such \(u\), the complete \(p\)-Apéry set at the first index beyond the regular range of Komatsu--Mu's Pell-triple formula is
\[
 \operatorname{Ap}_p(a,b,c)=\left\{(ps+j)b+zc-(s-1)a\,\mathbf1_{\{j=s-1\}}:
 0\le j<s,\ 0\le z<u\right\}.
\]
Consequently, the \(p\)-Frobenius number \(g_p=\max\{N\ge0:d(N)\le p\}\) and \(p\)-genus \(n_p=\#\{N\ge0:d(N)\le p\}\) are exactly
\[
 \boxed{g_p=(s^2-s-1)b+(u-1)c-sa},
\]
\[
 \boxed{n_p=psb+\frac{(s-1)b+(u-1)c-a+1}{2}-u(s-1)}.
\]
The regular rectangular Apéry pattern extrapolated to this first excluded index must be corrected in precisely the \(u\) residues corresponding to \(j=s-1\). Its predicted \(g_p\) is too large by \((s-1)a\), and its predicted \(n_p\) is too large by \(u(s-1)\).

## Assumptions and scope

The result holds for every integer \(u\ge2\) and only at \(p=u^2\), for the ordered generating triple \((P_4(u),P_6(u),P_9(u))\). In particular \(a<b<c\) and \(\gcd(a,b,c)=1\). Representations are ordered by generator type, not permutations of coins; each triple of nonnegative coefficients counts once. Values of \(N\) start at zero. The statement does not claim a formula for larger \(p\) or for other Pell index triples.

## Proof

Write \(h=s-1=u^2+1=P_3(u)\), \(v=s^2-1\), and \(q=s^2-s-1=P_5(u)\). The Pell recurrence, or expansion of the relevant polynomials, gives
\[
 a=us,\quad b=uv,\quad c=qv-sh,\quad v\equiv-1\pmod s,\quad c\equiv1\pmod u.
\]
Also \(q=(p+1)s-1\). Indeed, expansion gives \(c=(u^2+1)(u^6+6u^4+9u^2+1)\), so
\[
 c-sh=(u^2+1)(u^6+6u^4+8u^2-1)>0\qquad(u\ge2).
\]
Thus \(qv=c+sh<2c\), and \(v>s\). The identity \(c\equiv1\pmod u\) implies \(\gcd(a,b,c)=1\), because \(\gcd(s,v)=1\).

Fix \(0\le j<s\) and \(0\le z<u\), and put \(T=(ps+j)b+zc\). For any integer \(k\) with \(0\le k\le s\), count representations of \(T-ka\). Reduction modulo \(u\) forces the coefficient of \(c\) to be \(Z=z+ut\) for some integer \(t\ge0\). Since all coefficients are nonnegative,
\[
 tc\le (ps+j)v\le qv<2c,
\]
so \(t\in\{0,1\}\). Dividing the representation equation by \(u\) and substituting \(c=qv-sh\) yields
\[
 sx+Yv=(ps+j-tq)v+s(th-k).
\]
For \(t=0\), reduction modulo \(s\) gives precisely
\[
 Y=j+(p-\ell)s,\qquad x=\ell v-k,\qquad \ell\in\{0,1,\ldots,p\}.
\]
When \(k=0\), all \(p+1\) choices are valid; when \(1\le k\le s\), exactly \(\ell=1,\ldots,p\) are valid, since \(s<v\).

For \(t=1\), using \(ps-q=-h\) gives
\[
 Y=j-h+s\ell,\qquad x=h-k-\ell v.
\]
If \(j\le s-2\), nonnegative \(Y\) requires \(\ell\ge1\), which makes \(x<0\). If \(j=s-1=h\), nonnegative \(Y\) requires \(\ell\ge0\), and precisely \(\ell=0\) works when \(0\le k\le h\); no such representation exists for \(k=h+1=s\).

Therefore \(d(T)=p+1\) and \(d(T-a)=p\) for \(j\le s-2\), while \(d(T-ha)=p+1\) and \(d(T-(h+1)a)=p\) for \(j=h\). For any integer \(N\), adding one copy of \(a\) embeds the representations of \(N\) injectively into those of \(N+a\); thus \(d(N+a)\ge d(N)\). The displayed numbers are consequently the first integers with more than \(p\) representations in their own residues modulo \(a\).

These residues are distinct: modulo \(u\) a proposed element is \(z\), because \(c\equiv1\pmod u\). After fixing \(z\), divide its difference with \(zc\) by \(u\); reduction modulo \(s\) yields \(jv\equiv-j\pmod s\). Thus the \(us=a\) proposed numbers represent all residues exactly once. The stated formula for \(\operatorname{Ap}_p\) follows.

For each fixed \(j\), the candidates increase with \(z\). Among \(j\le s-2\), they increase with \(j\). The final row is larger than the preceding row by
\[
 b-ha=u\bigl((s^2-1)-s(s-1)\bigr)=u(s-1)>0.
\]
Hence \(g_p\) equals the last-row last-column element minus \(a\): \(g_p=(ps+s-1)b+(u-1)c-ha-a=qb+(u-1)c-sa\).

Finally the standard Apéry sum identity, also obtained by counting the holes separately in each residue, is
\[
 n_p=\frac1a\sum_{m\in\operatorname{Ap}_p}m-\frac{a-1}{2}.
\]
Summing the rectangular part and subtracting \(h a\) from exactly \(u\) entries yields
\[
 n_p=psb+\frac{(s-1)b+(u-1)c-a+1}{2}-\frac{uha}{a},
\]
which is the asserted formula. The final correction equals \(u(s-1)\). This completes the proof.

## Verification

The accompanying standalone `verify.py` constructs \(P_4(u),P_6(u),P_9(u)\) recursively, checks distinct candidate residues, computes all representation counts independently using the product generating function \(\prod_{r\in\{a,b,c\}}(1-X^r)^{-1}\) via dynamic programming, and compares the threshold, maximum and hole count to the formulas for \(u=2,3,4,5\). Verified \((u,p,g_p,n_p)\) are \((2,4,2943,2332)\), \((3,9,64817,50364)\), \((4,16,687391,530288)\), and \((5,25,4586499,3523375)\). These are finite checks only; the proof above is what covers every \(u\ge2\).

## Relationship to prior work

Komatsu and Mu's *p-numerical semigroups of Pell triples* (arXiv:2307.08998, Theorems 1 and 2) gives a uniform formula for even-even-odd triples \((P_{2i}(u),P_{2i+2}(u),P_{2i+2k+1}(u))\) under the strict inequality \(p<u(P_{2k+1}(u)+1)/P_{2i}(u)-1\). For \(i=k=2\), the upper endpoint is exactly \(p<u^2\). Those theorems therefore do not imply the formulas above at \(p=u^2\), and direct extrapolation gives a provably incorrect answer. The first exceptional Apéry row explains the discrepancy.

The earlier generalized-Fibonacci manuscript of Komatsu, Laishram and Punyani (arXiv:2304.00443) has the different Jacobsthal recurrence \(J_n(v)=J_{n-1}(v)+vJ_{n-2}(v)\), rather than the Pell recurrence with variable first coefficient. Its stated theorem on \((a,va+b,vaJ_{k-1}(v)+bJ_k(v))\) does not give the first excluded Pell boundary for every \(u\ge2\).

Mu and Komatsu's 2024 study of three-term recurrence triples (Axioms 13(9), 608; openly accessible 2024 preprint) provides later low-\(p\) formulas in a different parameter range, with its stated main theorems requiring \(i\ge k\ge3\) for the triple \((W_i,W_{i+2},W_{i+k})\). The present triple has \((i,k)=(4,5)\) in that indexing and lies beyond the earlier Pell-specific \(p\)-range. Neither cited theorem directly covers the first excluded value. This is a comparison of mathematical hypotheses, not a claim that no broader result could exist elsewhere.

## Limitations

Only the first excluded \(p\) and the specified one-parameter Pell triple are classified. The original paper's separate 2025 journal edition could not be fully inspected; the accessible arXiv text and the 2024 recurrence-triple preprint were compared. Other unindexed or inaccessible literature might contain equivalent formulas. A finite verification table does not establish the infinite family independently of the argument given.

## References

1. T. Komatsu and J. Mu, *p-numerical semigroups of Pell triples*, arXiv:2307.08998 (first posted July 18, 2023; v2 January 4, 2024), Theorems 1--2 and Lemma 1. https://arxiv.org/abs/2307.08998
2. J. Mu and T. Komatsu, *p-Numerical Semigroups of Triples from the Three-Term Recurrence Relations*, Axioms 13 (2024), article 608, DOI 10.3390/axioms13090608. Open preprint: https://www.preprints.org/manuscript/202407.1982
3. T. Komatsu, S. Laishram and P. Punyani, *p-numerical semigroup of generalized Fibonacci triples*, arXiv:2304.00443 (April 2023). https://arxiv.org/abs/2304.00443
