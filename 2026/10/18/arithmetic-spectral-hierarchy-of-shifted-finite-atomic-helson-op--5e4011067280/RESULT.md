# Arithmetic spectral hierarchy of shifted finite-atomic Helson operators

## Finding

**Theorem (full positive-eigenvalue hierarchy).** Fix an integer \(m\ge 1\), strictly increasing real numbers \(0<s_1<\cdots<s_m\), and weights \(w_1,\ldots,w_m>0\). For \(R\ge1\), let \(H_R\) be the positive Helson operator on \(\ell^2(\mathbb N)\) with matrix entries
\[
(H_R)_{a,b}=\sum_{j=1}^{m}w_j(ab)^{-(R+s_j)},\qquad a,b\ge1.
\]
For each positive integer \(n\), introduce \(v_n=(\sqrt{w_j}\,n^{-s_j})_{j=1}^m\in\mathbb R^m\), and define the positive Gram determinants
\[
\Delta_0=1,\qquad
\Delta_k=\det\bigl[(\langle v_a,v_b\rangle)_{1\le a,b\le k}\bigr],\quad 1\le k\le m.
\]
Then \(\Delta_k>0\) for all \(1\le k\le m\). The operator \(H_R\) has rank exactly \(m\), with ordered positive eigenvalues \(\lambda_1(R)\ge\cdots\ge\lambda_m(R)>0\), and for each fixed \(1\le k\le m\) it satisfies
\[
\boxed{\lambda_k(R)
=\frac{\Delta_k}{\Delta_{k-1}}\,k^{-2R}
\left[1+O_{m,\mathbf{s},\mathbf{w}}\!\left(\left(\frac{k}{k+1}\right)^{2R}\right)\right],\qquad R\longrightarrow+\infty.}
\]
In particular,
\[
\lim_{R\to\infty}\lambda_k(R)^{1/(2R)}=\frac1k,
\qquad
\lim_{R\to\infty}k^{2R}\lambda_k(R)=\frac{\Delta_k}{\Delta_{k-1}}>0.
\]
The exponential bases \(1,2,\ldots,m\) are independent of the atom locations and masses. For sufficiently large \(R\), all positive eigenvalues are simple. The sharp operator-norm error of the best rank-at-most-\(r\) approximation to \(H_R\) equals \(\lambda_{r+1}(R)\) and thus has the stated equivalent with \(k=r+1\) for each \(0\le r<m\).

## Assumptions and scope

All operators act on the complex Hilbert space \(\ell^2(\mathbb N)\) indexed from \(1\). The parameters \(m\), \(s_j\) and \(w_j\) are fixed as \(R\to\infty\); there is no uniformity assertion when the number of atoms, locations, or weights vary with \(R\). The assumption \(s_j>0\) is convenient for uniform bounds on the vectors \(v_n\); the same argument applies to fixed real atom offsets provided \(R+s_1>1/2\) eventually. The \(O\)-constants may depend on all fixed atom data.

The corresponding representing measure is \(\mu_R=\sum_{j=1}^{m}w_j\delta_{R+s_j}\). Its first public motivating source is the positive moment-form theory of Ma, Lu and Zu [1]. The result is an eigenvalue theorem for a specified finite-atomic family, not a boundedness or trace-class criterion for general measures.

## Proof

**1. Exact finite Gram representation.** Define \(T_R:\ell^2(\mathbb N)\to\mathbb C^m\) by \(T_Re_n=n^{-R}v_n\), using complex-linear extension. Because
\[
\sum_{n\ge1}\|n^{-R}v_n\|^2
=\sum_{j=1}^m w_j\zeta(2R+2s_j)<\infty,
\]
\(T_R\) is Hilbert–Schmidt and \(H_R=T_R^*T_R\) is positive trace class. The nonzero eigenvalues of \(H_R\), including multiplicity, coincide with those of
\[
G_R=T_RT_R^*=\sum_{n\ge1}n^{-2R}v_nv_n^*,\qquad
(G_R)_{ij}=\sqrt{w_iw_j}\,\zeta(2R+s_i+s_j).
\]
The last identity is exact for every \(R\ge1\).

**2. Nonvanishing of the leading minors.** For every \(k\le m\), the \(k\times k\) matrix \([a^{-s_j}]_{1\le a,j\le k}\) is nonsingular. Indeed a nonzero real exponential polynomial with \(k\) distinct real exponents has at most \(k-1\) distinct real zeros: multiply by the exponential of the smallest exponent and induct using Rolle's theorem on its derivative. Since \(\log 1,\ldots,\log k\) are distinct, singularity would contradict this zero bound. Multiplying columns by \(\sqrt{w_j}>0\) proves that \(v_1,\ldots,v_k\) are linearly independent, hence \(\Delta_k>0\). In particular \(G_R\) and \(H_R\) have exactly \(m\) positive eigenvalues for every \(R\ge1\).

**3. Exterior-power expansion.** For \(1\le k\le m\), write \(u_I=v_{n_1}\wedge\cdots\wedge v_{n_k}\in\bigwedge^k\mathbb C^m\) and \(p_I=n_1\cdots n_k\) for any increasing \(k\)-tuple \(I=(n_1<\cdots<n_k)\). Apply the compound-operator identity \(\bigwedge^k(T_RT_R^*)=(\bigwedge^kT_R)(\bigwedge^kT_R)^*\), first to finite column truncations and then by trace-norm convergence. This yields the norm-convergent positive rank-one expansion
\[
\bigwedge{}^kG_R=\sum_{n_1<\cdots<n_k}p_I^{-2R}\,u_Iu_I^*.
\]
The unique tuple with minimal product is \(I_0=(1,2,\ldots,k)\), with \(p_{I_0}=k!\) and \(\|u_{I_0}\|^2=\Delta_k\). All other tuples obey
\[
p_I\ge (k-1)!(k+1)=k!\frac{k+1}{k}=:p_{1,k}.
\]
For \(R\ge1\), put \(M=\sum_{j=1}^mw_j\), so \(\|v_n\|^2\le M\). Because the exterior norm is bounded by the product of vector norms,
\[
\sum_{I}\frac{\|u_I\|^2}{p_I^2}
\le\frac{M^k}{k!}\left(\sum_{n\ge1}n^{-2}\right)^k<\infty.
\]
Consequently the sum of nonleading terms has operator norm at most its trace and is bounded by
\[
\sum_{I\ne I_0}p_I^{-2R}\|u_I\|^2
\le p_{1,k}^{-2(R-1)}\sum_{I\ne I_0}p_I^{-2}\|u_I\|^2
=O_{m,\mathbf{s},\mathbf{w}}(p_{1,k}^{-2R}).
\]
The leading summand has norm exactly \(\Delta_k/(k!)^{2R}\). The triangle inequality and positivity therefore give
\[
\left\|\bigwedge{}^kG_R\right\|
=\frac{\Delta_k}{(k!)^{2R}}
\left[1+O_{m,\mathbf{s},\mathbf{w}}\!\left(\left(\frac{k}{k+1}\right)^{2R}\right)\right].
\]

**4. Isolation of individual eigenvalues.** The norm of the \(k\)-th exterior power of a positive matrix is the product of its \(k\) largest eigenvalues. Write \(L_k(R)=\prod_{j=1}^k\lambda_j(R)\) and \(L_0(R)=1\). The preceding identity gives the asymptotic for \(L_k(R)\). Divide the identities for \(L_k(R)\) and \(L_{k-1}(R)\). For \(k\ge2\), the latter error decays at rate \(((k-1)/k)^{2R}\), which is faster than \((k/(k+1))^{2R}\). For \(k=1\), take only the numerator. Thus
\[
\lambda_k(R)=\frac{\Delta_k}{\Delta_{k-1}}k^{-2R}
\left[1+O_{m,\mathbf{s},\mathbf{w}}\!\left(\left(\frac{k}{k+1}\right)^{2R}\right)\right].
\]
In particular \(\lambda_{k+1}(R)/\lambda_k(R)\to0\) for all \(k<m\), giving eventual simplicity. The rank-approximation statement is the standard compact-Hilbert-space singular-value minimax principle applied to the now explicit eigenvalue asymptotics. \(\square\)

## Verification

The independent analytical checks are: (i) the Dirichlet columns are square-summable for every specified \(R\); (ii) the exponential-polynomial zero bound establishes strictly positive leading Gram minors; (iii) the unique second-smallest tuple product is \((k-1)!(k+1)\); (iv) the positive exterior-power tail is bounded by a convergent \(\zeta(2)\) majorant; (v) the consecutive top-eigenvalue product ratio has the stated error rate.

For a reproducible exact finite diagnostic, `CHECKER.py` uses rational vectors \(v_n=(n^{-1},2n^{-2},3n^{-3})\) and verifies Cauchy–Binet exterior-minor identities on finite column sets, positivity and leading-term bounds. It also verifies the exact constants
\[
(\Delta_0,\Delta_1,\Delta_2,\Delta_3)
=\left(1,14,\frac{133}{64},\frac1{324}\right).
\]
These finite checks are diagnostics only: the infinite-dimensional result follows from the convergent tail estimate in the proof.

## Relationship to prior work

Ma, Lu and Zu [1] study the general positive Helson moment forms and prove operator closability, domain formulas, and a trace-class criterion. Their trace identity determines the sum of eigenvalues but not their individual asymptotics as an atomic representing measure translates to infinity. Perfekt and Pushnitski [2, Sections 5–6] give the zeta-kernel correspondence and characterize finite-rank Helson forms; the present Gram correspondence is an instance of that known result. Neither their finite-rank classification nor their zeta-kernel equivalence supplies the arithmetic separation rates \(k^{-2R}\) or determinant-ratio coefficients without the exterior-power asymptotic argument above. Miheisi and Pushnitski [3] prove a different infinite-rank eigenvalue asymptotic, indexed by eigenvalue rank tending to infinity for a fixed logarithmic symbol. That result is not the fixed-rank, translated-atomic limit here. Chavan, Sahu and Sinha [4] give norm, Schatten-class and scattering theory for measure-induced Helson operators on indices starting at \(2\); their stated theorems do not supply this translated finite-atomic full spectral profile.

## Limitations

The theorem assumes fixed finitely many distinct positive real atomic offsets and fixed strictly positive weights; it does not address colliding atoms, weights changing with \(R\), infinite measures, or a regime where \(k\) grows. It establishes eigenvalue magnitudes and finite-rank approximation errors, not eigenvector asymptotics or an inverse identification of all atom parameters from finitely many coefficients. While the listed sources were compared by statements and implications, an unlocated general theorem on strongly separated sums of rank-one operators might imply the same coefficient law; publication priority is therefore not independently certified.

## References

[1] T. Ma, Y. Lu, and C. Zu, *Unbounded Helson Forms with a Moment Representation*, arXiv:2610.12252v1 (first public 2026-10-08), https://arxiv.org/html/2610.12252v1.

[2] K.-M. Perfekt and A. Pushnitski, *On Helson matrices: moment problems, non-negativity, boundedness, and finite rank*, arXiv:1611.03772; Proc. London Math. Soc. 116 (2018), 101–134. https://arxiv.org/abs/1611.03772.

[3] N. Miheisi and A. Pushnitski, *A Helson matrix with explicit eigenvalue asymptotics*, arXiv:1709.06326v1 (2017), https://arxiv.org/html/1709.06326v1.

[4] S. Chavan, C. K. Sahu, and K. B. Sinha, *Helson matrices induced by measures*, arXiv:2407.04124v2 (original first public 2024-07-04), https://arxiv.org/html/2407.04124v2.
