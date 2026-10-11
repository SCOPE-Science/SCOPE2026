# Exact fourth-moment norm and deficit for a subgroup hole in a finite dual group
## Finding
Let \(G\) be a finite abelian group of order \(N\), let \(K\le \widehat G\) be a proper subgroup of order \(k\), and put \(H=K^\perp\), so \(|H|=m=N/k\ge2\). Set \(\Lambda=\widehat G\setminus K\). With normalized counting measure on \(G\), the sharp constant in
\[
\left\|\sum_{\chi\in\Lambda}a_\chi\chi\right\|_4
\le K_4(\Lambda)\left(\sum_{\chi\in\Lambda}|a_\chi|^2\right)^{1/2}
\]
is
\[
K_4(\Lambda)^4
= k\left(m-2+\frac1{m-1}\right)
=\frac{k(m^2-3m+3)}{m-1}.
\]
Moreover, the sharp inequality has an exact two-scale deficit decomposition. For each coset \(C\) of \(H\), write \(z_C=f|_C\), \(S_C=\sum_{x\in C}|f(x)|^2\), and let \(V_C=\{z\in\mathbb C^C:\sum_{x\in C}z_x=0\}\). Put \(d=m-1\), \(p_x=e_x-m^{-1}\mathbf1_C\in V_C\),
\[
W_C=\operatorname{span}_{\mathbb R}\left\{p_xp_x^*-\frac1m I_{V_C}:x\in C\right\},
\]
and
\[
R_C=z_Cz_C^*-\frac{S_C}{d}I_{V_C}
-\operatorname{Proj}_{W_C}\left(z_Cz_C^*-\frac{S_C}{d}I_{V_C}\right).
\]
If
\[
\alpha_m=\frac{m^2-3m+3}{m(m-1)},
\]
then
\[
N\left(K_4(\Lambda)^4\|f\|_2^4-\|f\|_4^4\right)
=2\alpha_m\sum_{C<D}S_CS_D
+\frac{m-2}{m}\sum_C\|R_C\|_{\mathrm{HS}}^2.
\]
In particular, for every \(y\in G\) and \(c\ne0\), the coefficient family
\[
a_\chi=c\,\overline{\chi(y)},\qquad \chi\in\Lambda,
\]
attains equality.

## Assumptions and scope
All groups are finite and abelian. The subgroup \(K\) is proper, so \(m\ge2\). Fourier characters are orthonormal for normalized counting measure. The statement gives the sharp \(L^2\)-to-\(L^4\) norm for the dense spectral set obtained by deleting an arbitrary subgroup of the dual, together with a quantitative identity for the entire deficit. It does not claim a classification of every equality case beyond the displayed extremizing family.

## Proof
Averaging over \(H\) is the Fourier multiplier of \(K\):
\[
\frac1{|H|}\sum_{h\in H}f(x+h)=0
\]
for every \(x\in G\), because \(f\) has no Fourier coefficient in \(K\). Hence on each coset \(C\) of \(H\), the vector \(z_C=f|_C\) lies in the zero-sum space \(V_C\).

It is therefore enough to prove the following local fourth-moment identity. Let \(V=\{z\in\mathbb C^m:\sum_jz_j=0\}\), \(d=m-1\), and \(p_j=e_j-m^{-1}\mathbf1\). Define \(E_j=p_jp_j^*\) and the Hilbert--Schmidt operator
\[
T(A)=\sum_{j=1}^m\operatorname{tr}(AE_j)E_j.
\]
For \(A=zz^*\),
\[
\langle A,T(A)\rangle_{\mathrm{HS}}=\sum_{j=1}^m|z_j|^4.
\]
The Gram matrix of the \(E_j\) has diagonal entry \(((m-1)/m)^2\) and off-diagonal entry \(1/m^2\), because \(\langle p_i,p_i\rangle=(m-1)/m\) and \(\langle p_i,p_j\rangle=-1/m\) for \(i\ne j\). Its two nonzero eigenvalues are therefore
\[
\lambda_0=\frac{m-1}{m}
\]
on the scalar direction and
\[
\lambda_1=\frac{m-2}{m}
\]
on the traceless span \(W=\operatorname{span}_{\mathbb R}\{E_j-m^{-1}I_V\}\).

Write \(S=\|z\|_2^2\) and
\[
B=zz^*-\frac{S}{d}I_V.
\]
Since \(zz^*\) has rank one,
\[
\|B\|_{\mathrm{HS}}^2=S^2\frac{m-2}{m-1}.
\]
The spectral decomposition of \(T\) gives the exact identity
\[
\sum_j|z_j|^4
=\frac{S^2}{m}+\frac{m-2}{m}\|\operatorname{Proj}_{W}B\|_{\mathrm{HS}}^2,
\]
hence
\[
\alpha_mS^2-\sum_j|z_j|^4
=\frac{m-2}{m}\|B-\operatorname{Proj}_{W}B\|_{\mathrm{HS}}^2.
\]
For \(m=2\), the coefficient \((m-2)/m\) is zero and the identity remains valid.

Apply this identity on every coset. If \(S=\sum_CS_C\) and \(Q=\sum_C\sum_{x\in C}|f(x)|^4\), then
\[
\alpha_mS^2-Q
=2\alpha_m\sum_{C<D}S_CS_D
+\frac{m-2}{m}\sum_C\|R_C\|_{\mathrm{HS}}^2.
\]
Because \(\|f\|_2^2=S/N\) and \(\|f\|_4^4=Q/N\), this is the stated global deficit identity and yields
\[
K_4(\Lambda)^4=N\alpha_m
=k\left(m-2+\frac1{m-1}\right).
\]

For sharpness, fix \(y\in G\) and take \(a_\chi=c\overline{\chi(y)}\) on \(\Lambda\). Character orthogonality gives
\[
f(x)=c\left(N\mathbf1_{\{y\}}(x)-k\mathbf1_{y+H}(x)\right).
\]
Thus all \(L^2\) mass lies on one coset, where the values are proportional to \((m-1,-1,\ldots,-1)\). Both nonnegative terms in the deficit identity vanish, so equality holds.

## Verification
The accompanying `verify.py` checks the exact rational identity for the two frame eigenvalues for every \(2\le m\le40\), stress-tests the inequality for cyclic groups of orders \(4\) through \(32\) over every proper dual subgroup, and replays the displayed character-evaluation extremizers. It returns:

`VERIFY_OK exact_m=2..40 random_checks=2040 cyclic_extremizers=85`

These computations are checks of the algebra and normalization; the proof above is finite-dimensional and does not rely on the random tests.

## Relationship to prior work
Michels, arXiv:math/9904176v1, gives the standard \(\Lambda(p)\) framework for character sets on compact abelian groups, but its main results concern infinite \(\Lambda(p)\)-sets and operator ideals rather than exact finite subgroup-hole constants. Bonami and Révész, arXiv:0811.4576v1, explicitly develop finite cyclic harmonic-analysis problems and relative concentration on cosets; their finite-group results concern idempotent concentration and do not state the present \(L^4/L^2\) subgroup-complement norm or its Hilbert--Schmidt deficit identity.

The previously known co-singleton case \(K=\{1\}\) is recovered by setting \(k=1\). The present theorem is not merely that specialization repeated: the subgroup hole forces a cosetwise conditional-mean decomposition, and the exact deficit separates loss from distributing energy among annihilator cosets from loss inside each zero-sum fiber.

## Limitations
The theorem is specific to the fourth moment. The simplex-frame diagonalization uses the quadratic structure of \(|z|^4\), and no all-even analogue is claimed. The full equality set is not classified here; only a sharp extremizing family is proved. A residual literature risk remains that the norm formula, without the deficit identity, may have appeared under finite-dimensional Nikolskii or zero-conditional-expectation terminology not captured by the searches below.

## References
1. C. Michels, *\(\Lambda(p)\)-sets and the limit order of operator ideals*, arXiv:math/9904176v1, first public 1999-04-30.
2. A. Bonami and S. Gy. Révész, *Concentration of the integral norm of idempotents*, arXiv:0811.4576v1, first public 2008-11-27, MSC 42A05; 42A16.
