# Exact seventh and eighth totient-prime thresholds

Let
\[
N_k=\min\{N:\phi(n)>k\pi(n)\text{ for every }n\ge N\},
\]
and, with \(A(n)=\pi(n)-\omega(n)\) and \(B(n)=\phi(n)-\pi(n)+\omega(n)\), let
\[
M_k=\min\{M:B(n)>kA(n)\text{ for every }n\ge M\}.
\]
Fatehizadeh determined \(N_1,\ldots,N_6\) and \(M_1,\ldots,M_5\), found \(M_k=N_{k+1}\) for \(1\le k\le5\), and conjectured this equality for every \(k\ge1\). The next two levels can be determined exactly.

## Theorem

Put \(P_r=p_r^\#=\prod_{j\le r}p_j\). Then
\[
\boxed{N_7=M_6=290239045397854538365381}
\]
and
\[
\boxed{N_8=M_7=4015602312602016465554214991}.
\]
Equivalently, the last failures of \(\phi(n)>7\pi(n)\) and \(\phi(n)>8\pi(n)\) are respectively
\[
L_7=290239045397854538365380
    =2P_{18}\frac{73}{59},
\]
\[
L_8=4015602312602016465554214990
    =7P_{20}\frac{73}{71}.
\]
Both boundary integers also fail the corresponding nonprime-totative inequalities \(B(n)>6A(n)\) and \(B(n)>7A(n)\). Thus Fatehizadeh's threshold-equality conjecture holds for the two additional cases \(k=6,7\).

## Explicit analytic bounds

The proof uses the explicit prime-counting bounds of Axler. For \(y=\log x\), define
\[
U(y)=y-1-y^{-1}-3.15y^{-2}-12.85y^{-3}-71.3y^{-4}-463.2275y^{-5}-4585y^{-6},
\]
\[
D(y)=y-1-y^{-1}-2.85y^{-2}-13.15y^{-3}-70.7y^{-4}-458.7275y^{-5}-3428.7225y^{-6}.
\]
Axler proves
\[
\pi(x)<\frac{x}{U(\log x)}\quad(x\ge49),
\qquad
\pi(x)>\frac{x}{D(\log x)}\quad(x\ge19033744403).
\]
We also use the Rosser--Schoenfeld estimate
\[
\frac n{\phi(n)}<e^\gamma\log\log n+\frac{2.50637}{\log\log n}\qquad(n\ge3).
\]
Finally, if \(r=\omega(n)\), primorial extremality gives
\[
\frac n{\phi(n)}\le\frac{P_r}{\phi(P_r)}.
\]

## Boundary failures

The two boundary factorizations have \(\omega(L_7)=18\), \(\omega(L_8)=20\), and
\[
\phi(L_7)=38318071049103605760000,
\]
\[
\phi(L_8)=513385515915890109972480000.
\]
The Axler lower bound gives, with conservative directed numerical evaluation,
\[
\frac{L_7}{D(\log L_7)}-\frac{\phi(L_7)}7
>1.63905706537\times10^{18},
\]
\[
\frac{L_8}{D(\log L_8)}-\frac{\phi(L_8)}8
>3.17709405090\times10^{22}.
\]
These margins are much larger than the corrections \(18\) and \(20\), respectively. Hence
\[
\phi(L_7)<7(\pi(L_7)-18),\qquad
\phi(L_8)<8(\pi(L_8)-20).
\]
Therefore \(L_7\) fails both \(\phi>7\pi\) and \(B>6A\), while \(L_8\) fails both \(\phi>8\pi\) and \(B>7A\).

## Excluding later failures at level 7

Let \(C_7=4P_{18}\). If \(L_7<n<C_7\) and \(\omega(n)\le17\), then
\[
\frac{\phi(n)}{\pi(n)}
>\frac{\phi(P_{17})}{P_{17}}U(\log L_7)
>7.0910757,
\]
so only \(\omega(n)=18\) remains.

Write \(d=\operatorname{rad}(n)\) and \(n=md\). Since \(d\ge P_{18}\) and \(n<C_7=4P_{18}\), one has \(m\in\{1,2,3\}\). If \(q\) is the largest prime in the support of \(d\), then
\[
qP_{17}\le d<C_7=244P_{17},
\]
so \(q\le241\). Thus the remaining range reduces to finitely many 18-element prime supports and the admissible multipliers \(m\). Exact support enumeration leaves 2202 values in \((L_7,C_7)\); every one satisfies the stronger certified comparison
\[
\phi(n)>7\frac{n}{U(\log n)}>7\pi(n).
\]
The smallest verified margin \(\phi(n)-7n/U(\log n)\) is greater than \(1.1549\times10^{18}\).

For \(C_7\le n<P_{19}\), one has \(\omega(n)\le18\), and
\[
\frac{\phi(P_{18})}{P_{18}}U(\log C_7)-7>0.0380444,
\]
which excludes every failure in this interval.

## Excluding later failures at level 8

Let \(C_8=8P_{20}\). If \(L_8<n<C_8\) and \(\omega(n)\le19\), then
\[
\frac{\phi(n)}{\pi(n)}
>\frac{\phi(P_{19})}{P_{19}}U(\log L_8)
>8.1070879,
\]
so only \(\omega(n)=20\) remains.

Again write \(n=md\) with \(d=\operatorname{rad}(n)\). Now \(d\ge P_{20}\), hence \(m<8\). The largest support prime satisfies
\[
qP_{19}\le d<C_8=568P_{19},
\]
so \(q\le563\). Exhausting the corresponding 20-element prime supports and all \(1\le m\le7\) whose prime divisors lie in the support gives 19710 values in \((L_8,C_8)\). Every value satisfies
\[
\phi(n)>8\frac{n}{U(\log n)}>8\pi(n),
\]
with smallest certified margin greater than \(6.987\times10^{23}\).

For \(C_8\le n<P_{21}\), primorial extremality gives
\[
\frac{\phi(P_{20})}{P_{20}}U(\log C_8)-8>0.0064221,
\]
so this interval contains no further failure.

## The global tail

For \(x\ge P_{19}\), combine Rosser--Schoenfeld and Axler to obtain
\[
\frac{\phi(n)}{\pi(n)}>
Q(n):=
\frac{U(\log n)}{e^\gamma\log\log n+2.50637/\log\log n}.
\]
The function \(Q\) is increasing throughout the range needed here. Indeed, with \(y=\log n\) and \(u=\log y\), one has \(U'(y)>1\) and \(U(y)<y\), hence
\[
\frac{d}{dy}\log U(y)>\frac1y.
\]
For \(H(u)=e^\gamma u+2.50637/u\),
\[
\frac{d}{dy}\log H(u)<\frac1{uy},
\]
so \(d(\log Q)/dy>(1-1/u)/y>0\).

Conservative evaluation gives
\[
Q(P_{19})>7.1908541,
\qquad
Q(P_{21})>8.0499974.
\]
Thus all \(n\ge P_{19}\) satisfy \(\phi(n)>7\pi(n)\), and all \(n\ge P_{21}\) satisfy \(\phi(n)>8\pi(n)\). Together with the preceding finite ranges, this proves that \(L_7,L_8\) are the exact last failures.

Finally, the identity
\[
B(n)-kA(n)=\phi(n)-(k+1)\pi(n)+(k+1)\omega(n)
\]
implies \(M_k\le N_{k+1}\). Since the two boundary integers above are also failures of the appropriate \(B>kA\) inequalities, equality follows for \(k=6,7\).

## Reproducibility

`artifacts/verify.py` uses only the Python standard library. It reconstructs the relevant primorials and boundary factorizations, evaluates the explicit Axler and Rosser--Schoenfeld bounds with high-precision decimal arithmetic and conservative widening, exhausts the finite radical-support ranges described above, and checks all displayed positive margins. The expected output is recorded in `artifacts/verify-output.txt`.

## Literature context and limitations

Fatehizadeh's 12 September 2026 preprint proves \(M_k\le N_{k+1}\) in general, determines \(N_1,\ldots,N_6\) and \(M_1,\ldots,M_5\), and formulates \(M_k=N_{k+1}\) as Conjecture 3.5. The present result supplies the next two exact threshold pairs. The explicit prime-counting estimates used here are from Axler, and the totient lower bound is due to Rosser and Schoenfeld.

Originality is asserted only to the best of our knowledge. Searches for the exact boundary integers, the phrases `N_7`, `N_8`, `M_6=N_7`, `M_7=N_8`, the inequalities \(\phi(n)>7\pi(n)\), \(\phi(n)>8\pi(n)\), and follow-ups to the motivating preprint found no prior determination of these two threshold pairs. Because the motivating paper is very recent, an unindexed contemporaneous follow-up remains a residual risk. No highly relevant inaccessible paper was identified.

This result does not prove Conjecture 3.5 for all \(k\), nor does it claim that the displayed finite-enumeration pattern persists at higher levels.

## References

1. A. Fatehizadeh, *Prime and Nonprime Totatives: A Sharp Construction and Exact Thresholds*, arXiv:2609.13852 (2026). https://arxiv.org/abs/2609.13852
2. C. Axler, *New estimates for some functions defined over primes*, Integers 18 (2018), A52; arXiv:1703.08032. https://arxiv.org/abs/1703.08032
3. J. Barkley Rosser and L. Schoenfeld, *Approximate formulas for some functions of prime numbers*, Illinois J. Math. 6 (1962), 64--94. https://doi.org/10.1215/ijm/1255631807
