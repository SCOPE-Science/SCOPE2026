# The leading tail coefficient alone determines the quasi-homogeneous exponents
## Finding
For distinct positive integers \(k,\ell\), let
\[
M_{k,\ell}=[z^k-w^\ell]\subset H^2(\mathbb D^2)
\]
and let \(C_{k,\ell}\) be the leading coefficient in Yang's numerical-invariant asymptotic
\[
\Sigma_j(M_{k,\ell})=\frac{C_{k,\ell}}{j}+O(j^{-2}).
\]
Then the scalar \(C_{k,\ell}\) alone determines the unordered pair \(\{k,\ell\}\). Equivalently, for distinct positive integers \(k,\ell,k',\ell'\),
\[
C_{k,\ell}=C_{k',\ell'}\quad\Longrightarrow\quad \{k,\ell\}=\{k',\ell'\}.
\]
Thus the single limit
\[
\lim_{j\to\infty}j\,\Sigma_j(M_{k,\ell})
\]
already determines \(\{k,\ell\}\). By the boundary formula for Yang's generating function, the same is true of the coefficient of \(\log(1/(1-t))\) at \(t=1\). In exact parameter recovery, neither the first strict descent nor the second-order boundary support is needed once this leading coefficient is known exactly.

## Assumptions and scope
The claim is restricted to the quasi-homogeneous bidisk submodules \(M_{k,\ell}=[z^k-w^\ell]\) with \(k,\ell\in\mathbb N\) and \(k\ne\ell\). It is an exact-identifiability statement. No quantitative lower bound is claimed for the separation between two distinct coefficients, so the result does not by itself give a numerically stable reconstruction procedure from finite-precision data.

Write
\[
a=\min\{k,\ell\},\qquad b=\max\{k,\ell\},\qquad r=\frac ba>1.
\]
The source gives
\[
C_{k,\ell}
=
\frac{ab(a+b)}{(b-a)^2}
-
\frac{2a^2b^2}{(b-a)^3}\log\frac ba
=
a\Phi(r),
\]
where
\[
\Phi(r)=A(r)-B(r)\log r,\qquad
A(r)=\frac{r(r+1)}{(r-1)^2},\qquad
B(r)=\frac{2r^2}{(r-1)^3}.
\]

## Proof
Suppose two unordered pairs give the same leading coefficient. Write the second pair as \(c<d\) and put \(s=d/c>1\). Then
\[
aA(r)-aB(r)\log r=cA(s)-cB(s)\log s.
\]
All of \(aA(r)\), \(aB(r)\), \(cA(s)\), and \(cB(s)\) are rational because \(a,c,r,s\) are rational. Hence
\[
q:=aA(r)-cA(s)=aB(r)\log r-cB(s)\log s
\]
is rational.

Choose a positive integer \(N\) clearing the denominators of the three rational numbers \(q\), \(aB(r)\), and \(cB(s)\). Then
\[
m\log r-n\log s=Q
\]
for integers \(m,n,Q\), with \(m,n>0\). Exponentiation gives
\[
\frac{r^m}{s^n}=e^Q.
\]
The left side is a positive rational number. If \(Q\ne0\), the Hermite--Lindemann theorem says that \(e^Q\) is transcendental because \(Q\) is a nonzero algebraic number, a contradiction. Therefore \(Q=0\), and hence \(q=0\). We obtain the two separate equalities
\[
aA(r)=cA(s),
\qquad
aB(r)\log r=cB(s)\log s.
\]

Dividing the second equality by the first yields
\[
\frac{B(r)}{A(r)}\log r
=
\frac{B(s)}{A(s)}\log s.
\]
A direct simplification gives
\[
\frac{B(u)}{A(u)}=\frac{2u}{u^2-1}
=\frac{1}{\sinh(\log u)}.
\]
Thus
\[
h(\log r)=h(\log s),
\qquad
h(x)=\frac{x}{\sinh x},\quad x>0.
\]
The function \(h\) is strictly decreasing on \((0,\infty)\), because
\[
h'(x)=\frac{\sinh x-x\cosh x}{\sinh^2x}<0;
\]
indeed \(x\cosh x-\sinh x\) vanishes at \(0\) and has derivative \(x\sinh x>0\) for \(x>0\). Consequently \(\log r=\log s\), so \(r=s\). The rational-part equality then becomes
\[
aA(r)=cA(r),
\]
and \(A(r)>0\), hence \(a=c\). Therefore \(b=ar=cs=d\), proving
\[
\{k,\ell\}=\{k',\ell'\}.
\]

## Verification
The proof uses only the published closed formula for \(C_{k,\ell}\), elementary algebra and monotonicity, and the classical Hermite--Lindemann theorem. The identity
\[
\frac{B(r)}{A(r)}=\frac{2r}{r^2-1}
\]
was checked algebraically, and the packaged finite stress test evaluates all unordered pairs \(1\le a<b\le200\) at high precision and finds no collision. That computation is only a diagnostic; the infinite injectivity statement is proved analytically above.

The source also identifies
\[
C_{k,\ell}=\lim_{j\to\infty}j\Sigma_j(M_{k,\ell})
=\lim_{t\to1^-}(1-t)\mathcal P'_{k,\ell}(t),
\]
so the parameter-recovery conclusion applies equally to the tail coefficient and to the leading logarithmic boundary coefficient.

## Relationship to prior work
Liu, Lu, and Yang proved the asymptotic formula for \(C_{k,\ell}\) and showed that the first strict descent together with \(C_{k,\ell}\) recovers \(\{k,\ell\}\). Their Remark 3.3 explicitly notes that this two-datum sufficiency statement does not assert that either datum alone is sufficient. The argument above resolves that particular minimal-data question for the leading coefficient: \(C_{k,\ell}\) is already injective on unordered pairs of distinct positive integers.

Their preceding paper determined the complete numerical-invariant sequence and showed that the full sequence recovers the unordered pair. That result does not supply single-scalar recovery. The present statement is therefore a strict reduction of the required asymptotic data, not a special case obtained by fixing parameters in a broader recovery theorem.

## Limitations
The theorem is exact rather than quantitative. It does not estimate
\[
|C_{k,\ell}-C_{k',\ell'}|
\]
for distinct pairs, and therefore it does not establish stability under measurement or numerical truncation. The proof also uses transcendence of \(e^\alpha\) for nonzero algebraic \(\alpha\); no elementary replacement is supplied. No claim is made for other families of bidisk submodules or for arbitrary numerical-invariant sequences.

## References
1. Yin Liu, Yufeng Lu, and Yixin Yang, *Asymptotic Rigidity and Boundary Structure of Yang's Numerical Invariants for the Bidisk Submodules \([z^k-w^\ell]\)*, arXiv:2609.36516v1, 29 September 2026.
2. Yin Liu, Yufeng Lu, and Yixin Yang, *Numerical Invariants and Parameter Recovery for Quasi-Homogeneous Submodules \([z^k-w^\ell]\)*, arXiv:2609.25640v1, 22 September 2026.
3. Lindemann--Weierstrass theorem (in particular the Hermite--Lindemann consequence that \(e^\alpha\) is transcendental for every nonzero algebraic \(\alpha\)).
