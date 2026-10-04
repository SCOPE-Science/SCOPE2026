# Frequency-deletion phase retrieval on cyclic groups: exact odd-order classification
## Finding
Let \(n\ge 2\), let \(G=\mathbb Z/n\mathbb Z\), and let \(\chi_m(x)=\exp(2\pi i mx/n)\). Write
\[
\mathcal H_0=\left\{f\in\mathbb C^G:\widehat f(0)=0\right\}.
\]
For every nonzero \(\ell\in G\), let \(P_\ell\) be the orthogonal Fourier projection that deletes the \(\ell\)-th Fourier coefficient and preserves all other coefficients. Then the following phase-retrieval property holds exactly when \(n\) is odd and \(n\ge5\):
\[
\bigl(|P_\ell f|=|P_\ell g|\text{ pointwise for every }\ell\ne0\bigr)
\quad\Longrightarrow\quad
f=\lambda g\text{ for some }|\lambda|=1,
\]
for all \(f,g\in\mathcal H_0\).

Thus every odd cyclic order \(n\ge5\), including every odd composite order, has the frequency-deletion phase-retrieval property, while every even order and the small orders \(2,3\) fail.

## Assumptions and scope
The Fourier transform may be taken with any fixed unitary or unnormalized convention; the proof uses only identities that are unchanged by a common normalization factor. The measurement \(|P_\ell f|\) is the pointwise modulus of the signal obtained after deleting one nonzero Fourier coefficient. The theorem concerns the complete family of all such deletions and the zero-mean subspace \(\mathcal H_0\). It does not claim stability bounds under noise, recovery from a proper subfamily of deletions, or an analogous classification for noncyclic finite abelian groups.

## Proof
Put \(a_m=\widehat f(m)\) and \(b_m=\widehat g(m)\), so \(a_0=b_0=0\). Equality of the pointwise squared moduli \(|P_\ell f|^2=|P_\ell g|^2\) implies equality of every Fourier coefficient of those squared moduli. Fix a nonzero shift \(r\in G\), and define
\[
d_m=a_{m+r}\overline{a_m}-b_{m+r}\overline{b_m},
\qquad
T=\sum_{m\in G}d_m.
\]
Because \(a_0=b_0=0\), one has \(d_0=d_{-r}=0\). Deleting frequency \(\ell\ne0\) removes exactly the two terms indexed by \(m=\ell\) and \(m=\ell-r\) from the \(r\)-shift autocorrelation. Hence
\[
T=d_\ell+d_{\ell-r}
\qquad(\ell\ne0).
\]
Let \(g_0=\gcd(n,r)\), and let \(q=n/g_0\) be the additive order of \(r\). If \(n\) is odd, then \(q\) is odd. On the \(r\)-cycle containing \(0\), write \(x_j=d_{jr}\). Since \(x_0=x_{q-1}=0\), the recurrence
\[
x_j+x_{j-1}=T
\]
forces \(x_j=T\) for odd \(j\) and \(x_j=0\) for even \(j\). Its contribution to \(\sum d_m\) is therefore \((q-1)T/2\). On every other \(r\)-cycle, the same recurrence closes around an odd cycle and has the unique solution \(d_m=T/2\), contributing \(qT/2\) per cycle. Therefore
\[
T=\sum_m d_m
 =T\left(\frac{q-1}{2}+(g_0-1)\frac q2\right)
 =T\frac{n-1}{2}.
\]
For odd \(n\ge5\), this forces \(T=0\), and then the recurrence gives \(d_m=0\) for every \(m\). Thus
\[
a_{m+r}\overline{a_m}=b_{m+r}\overline{b_m}
\]
for every nonzero shift \(r\) and every \(m\).

For the zero shift, let
\[
E_f=\sum_m|a_m|^2,
\qquad
E_g=\sum_m|b_m|^2.
\]
The same squared-modulus identity gives
\[
E_f-|a_\ell|^2=E_g-|b_\ell|^2
\qquad(\ell\ne0).
\]
Hence \(|a_\ell|^2-|b_\ell|^2=E_f-E_g\) for every nonzero \(\ell\). Summing over the \(n-1\) nonzero frequencies gives
\[
E_f-E_g=(n-1)(E_f-E_g),
\]
so \(E_f=E_g\) when \(n\ge3\), and consequently \(|a_\ell|=|b_\ell|\) for every \(\ell\). Together with the nonzero-shift identities, this yields equality of the full rank-one Fourier Gram matrices,
\[
a_j\overline{a_m}=b_j\overline{b_m}
\qquad(j,m\in G).
\]
Therefore either both vectors vanish or \(b=\lambda a\) for a unimodular scalar \(\lambda\), and Fourier inversion gives \(g=\lambda f\).

It remains to show that all excluded orders fail. If \(n\ge4\) is even, choose \(u=1\) and \(v=1+n/2\). Let the only nonzero Fourier coefficients of \(f\) be \(a_u=1,a_v=i\), and those of \(g\) be \(b_u=1,b_v=-i\). Since \(\chi_v(x)=\chi_u(x)(-1)^x\), the undeleted signals satisfy
\[
|f(x)|=|g(x)|
\]
for every \(x\). Deleting \(u\) or \(v\) leaves a single character of the same magnitude, while deleting any other nonzero frequency leaves the equal-modulus undeleted signals. Hence all deletion magnitudes agree, but \(f\) and \(g\) are not related by a global phase. For \(n=3\), Fourier coefficient pairs \((1,i)\) and \((1,-i)\) give the same data because each deletion leaves only one nonzero coefficient. For \(n=2\), the sole nonzero-frequency deletion annihilates every vector in \(\mathcal H_0\), so recovery is impossible.

## Verification
The accompanying `verify.py` checks the linear system extracted from the proof over the exact rational numbers. For every odd \(n\) from \(5\) through \(31\) and every nonzero shift \(r\), it verifies that the constraints
\[
d_0=d_{-r}=0,
\qquad
\sum_m d_m-d_\ell-d_{\ell-r}=0
\]
have only the zero solution. It also checks the zero-shift system and the explicit even-order and small-order failure mechanisms. Running `python verify.py` produces a single `VERIFY_OK` line. These finite checks are consistency tests only; the all-order statement is proved analytically above.

## Relationship to prior work
Bartusel, Führ, and Oussa derive the prime-field deletion observation in Remark 6.12 of arXiv:2109.07123 from their affine-group phase-retrieval construction. Their statement concerns prime order and explicitly asks whether the same observation holds for Fourier transforms on general cyclic groups. The theorem above answers that question completely: the property extends to every odd cyclic order at least \(5\), including composite orders, and fails for every even cyclic order as well as \(2\) and \(3\).

The proof does not use the affine-group representation. Instead it converts the deletion data into a family of autocorrelation equations and resolves them by the parity of the additive cycles generated by each frequency difference.

## Limitations
No quantitative stability estimate is proved. The theorem uses every nonzero frequency deletion; it does not determine the smallest subfamily of deletions sufficient for phase retrieval. The result is specific to cyclic groups and does not classify the corresponding problem on arbitrary finite abelian groups. The literature comparison is strongest against the explicit open question in the inspected source; an equivalent theorem under substantially different terminology remains a residual bibliographic risk.

## References
1. D. Bartusel, H. Führ, V. Oussa, *Phase retrieval for affine groups over prime fields*, arXiv:2109.07123. First public version: 2021-09-15. Remark 6.12 formulates the prime-order frequency-deletion observation and asks about general cyclic groups.
2. P. Grohs, S. Koppensteiner, M. Rathmair, *Phase retrieval: uniqueness and stability*, SIAM Review 62 (2020), 301–350. General phase-retrieval and Pauli-pair background cited by the primary source.
