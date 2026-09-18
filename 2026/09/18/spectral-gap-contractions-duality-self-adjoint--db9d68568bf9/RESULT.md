# Contractive spectral tails for compact duality-self-adjoint operators

## Statement

Let \(X\) be a smooth complex Banach space and let \(J:X\to X^*\) be its normalized duality map,
\[
\|Jx\|=\|x\|,\qquad Jx(x)=\|x\|^2.
\]
Let \(T\in\mathcal B(X)\) satisfy
\[
T^*Jx=J(Tx)\qquad(x\in X).
\]
Assume that \(T\) is compact.

For every nonzero spectral value \(\lambda\), let \(P_\lambda\) denote the Riesz projection of \(T\) at \(\lambda\). Then:

1. Every nonzero spectral value is real and semisimple:
   \[
   \ker (T-\lambda I)^2=\ker(T-\lambda I),
   \]
   hence \(\operatorname{ran}P_\lambda=\ker(T-\lambda I)\).

2. Every nonzero spectral projection is contractive:
   \[
   \boxed{\|P_\lambda\|=1.}
   \]

3. Let
   \[
   a_1>a_2>\cdots>0
   \]
   be the distinct positive numbers occurring as \(|\lambda|\) for
   \(\lambda\in\sigma(T)\setminus\{0\}\).  For
   \[
   Q_k=\sum_{|\lambda|\ge a_k}P_\lambda,\qquad R_k=I-Q_k,
   \]
   the residual projection is contractive whenever it is nonzero:
   \[
   \boxed{\|R_k\|=1},
   \qquad
   \boxed{\|Q_k\|\le 2}.
   \]
   If \(a_{k+1}\) exists, then the spectral tail has the exact norm
   \[
   \boxed{
   \left\|T-\sum_{|\lambda|\ge a_k}\lambda P_\lambda\right\|
   =a_{k+1}.
   }
   \]
   If there is no further nonzero spectral value, the displayed remainder is zero.

Consequently,
\[
T=\sum_{\lambda\in\sigma(T)\setminus\{0\}}\lambda P_\lambda
\]
converges in operator norm when the nonzero eigenvalues are taken in nonincreasing order of modulus, with the possible pair \(a,-a\) kept in the same modulus block.

There is also a useful single-eigenvalue formulation. Suppose the nonzero eigenvalues are extracted successively so that each next eigenvalue has maximal modulus in the current invariant residual, as in the induction used in arXiv:2608.06873v1. Let
\[
S_n=\sum_{j=1}^n\lambda_jP_{\lambda_j}.
\]
At any stage, at most one member of a sign pair \(\{a,-a\}\) can split the current modulus block. Therefore
\[
\boxed{\sup_n\left\|\sum_{j=1}^nP_{\lambda_j}\right\|\le 3}
\]
and, if \(\rho_n\) is the largest modulus of an omitted eigenvalue,
\[
\boxed{\|T-S_n\|\le 2\rho_n\longrightarrow0.}
\]
Thus the operator-norm convergence does not require contractivity of every arbitrary Auerbach residual projection.

## Proof

### 1. Two elementary consequences of duality self-adjointness

Smoothness makes \(J\) single-valued, and on a complex smooth Banach space it is conjugate-homogeneous:
\[
J(\alpha x)=\overline{\alpha}\,Jx.
\]

First,
\[
\|Tx\|^2
=J(Tx)(Tx)
=(T^*Jx)(Tx)
=Jx(T^2x)
\le \|x\|\,\|T^2x\|.
\]
Taking the supremum over \(\|x\|=1\) yields
\[
\|T\|^2\le \|T^2\|.
\]
The reverse inequality is automatic, so
\[
\|T^2\|=\|T\|^2.
\]
Every power of \(T\) is again duality-self-adjoint, since
\[
(T^m)^*Jx=J(T^m x).
\]
Iterating along powers \(2^r\) and using the spectral-radius formula gives
\[
\boxed{r(T)=\|T\|.}
\]
The same argument applies to every invariant restriction that remains duality-self-adjoint.

Next, if \(Tx=\lambda x\) with \(x\ne0\), then
\[
\lambda\|x\|^2
=Jx(Tx)
=(T^*Jx)(x)
=J(Tx)(x)
=\overline{\lambda}\|x\|^2.
\]
Hence every eigenvalue is real. Since every nonzero spectral value of a compact operator is an eigenvalue, the nonzero spectrum of \(T\) is real.

### 2. Nonzero eigenvalues are semisimple

Let \(0\ne u\in\ker(T-\lambda I)\), where \(\lambda\ne0\). Since \(\lambda\) is real,
\[
T^*Ju=J(Tu)=J(\lambda u)=\lambda Ju.
\]
If \((T-\lambda I)v=u\), then
\[
\|u\|^2
=Ju(u)
=Ju((T-\lambda I)v)
=((T^*-\lambda I)Ju)(v)
=0,
\]
a contradiction. Thus no Jordan chain of length two exists at a nonzero eigenvalue. For an isolated nonzero spectral value of a compact operator this implies that its generalized eigenspace is exactly its eigenspace. Therefore
\[
\operatorname{ran}P_\lambda=\ker(T-\lambda I).
\]

### 3. Each individual nonzero Riesz projection is contractive

Fix \(\lambda\ne0\). Write the canonical Riesz decomposition
\[
X=E_\lambda\oplus N_\lambda,
\qquad
E_\lambda=\ker(T-\lambda I),
\qquad
N_\lambda=\ker P_\lambda.
\]
Both summands are \(T\)-invariant and
\[
\lambda\notin\sigma(T|_{N_\lambda}).
\]

For \(m\in E_\lambda\) and \(z\in N_\lambda\), choose
\(y\in N_\lambda\) such that
\[
z=(T-\lambda I)y.
\]
Then, using the norming functional of \(m\),
\[
Jm(z)
=Jm(Ty)-\lambda Jm(y)
=(T^*Jm)(y)-\lambda Jm(y)
=0.
\]
Thus, for \(x=m+z\),
\[
\|m\|^2=Jm(m)=Jm(x)\le \|m\|\,\|x\|.
\]
Hence \(\|m\|\le\|x\|\), which is precisely
\[
\|P_\lambda x\|\le\|x\|.
\]
Since \(P_\lambda\) is nonzero,
\[
\|P_\lambda\|=1.
\]

This also identifies the Auerbach projection used in the inductive construction of arXiv:2608.06873v1 with the canonical Riesz projection. Indeed, if
\((e_i)\) is an Auerbach basis of \(E_\lambda\), smoothness makes its norm-one Hahn--Banach coordinate extensions equal to \(Je_i\). The intersection
\[
N=\bigcap_i\ker Je_i
\]
is \(T\)-invariant, complementary to \(E_\lambda\), and cannot have \(\lambda\) in the spectrum of \(T|_N\): compactness would otherwise make \(\lambda\) an eigenvalue on \(N\), contradicting \(E_\lambda\cap N=\{0\}\). Hence this is exactly the Riesz complement.

### 4. A spectral gap forces the entire residual projection to be contractive

More generally, let \(F\) be a finite set of nonzero eigenvalues and let
\[
M=\bigoplus_{\lambda\in F}E_\lambda,\qquad X=M\oplus N
\]
be the corresponding Riesz decomposition. Assume
\[
r(T|_N)<\min_{\lambda\in F}|\lambda|.
\]
Let \(R\) be the projection onto \(N\) along \(M\).

Take \(z\in N\), \(m_\lambda\in E_\lambda\), and \(k\ge0\). Iterating
\(T^*J=JT\) gives
\[
(T^*)^kJz=J(T^kz).
\]
Therefore
\[
\lambda^k Jz(m_\lambda)
=J(T^kz)(m_\lambda).
\]
Consequently
\[
|Jz(m_\lambda)|
\le
\frac{\|T^kz\|\,\|m_\lambda\|}{|\lambda|^k}
\longrightarrow0,
\]
because \(r(T|_N)<|\lambda|\). Hence \(Jz(m_\lambda)=0\) for every
\(\lambda\in F\), and by linearity of the functional \(Jz\),
\[
Jz(M)=0.
\]
Writing \(x=m+z\) gives
\[
\|z\|^2=Jz(z)=Jz(x)\le\|z\|\,\|x\|,
\]
so \(\|z\|\le\|x\|\). Thus
\[
\boxed{\|R\|\le1}.
\]
If \(N\ne\{0\}\), equality holds.

This is the point at which the operator dynamics matter: an arbitrary residual projection produced from unrelated Auerbach data need not be contractive, but a genuine spectral residual separated by a modulus gap is.

### 5. Exact tails

For the modulus levels \(a_k\), the set
\[
F_k=\{\lambda\in\sigma(T):|\lambda|\ge a_k\}
\]
is finite. Its residual spectrum has radius \(a_{k+1}<a_k\) when a next level exists. Step 4 therefore yields
\[
\|R_k\|=1
\]
unless \(R_k=0\), and hence \(\|Q_k\|\le2\).

The closed subspace \(N_k=R_kX\) is smooth. Its normalized duality map is simply
\[
J_{N_k}z=(Jz)|_{N_k},
\]
because the restriction still has norm \(\|z\|\) and norms \(z\). Moreover
\(T_k=T|_{N_k}\) remains duality-self-adjoint:
\[
T_k^*J_{N_k}z=J_{N_k}(T_kz).
\]
By Step 1,
\[
\|T_k\|=r(T_k).
\]
Therefore, when \(a_{k+1}\) exists,
\[
\|T_k\|=a_{k+1}.
\]

Since the nonzero eigenvalues are semisimple,
\[
TQ_k=\sum_{|\lambda|\ge a_k}\lambda P_\lambda,
\]
and
\[
T-\sum_{|\lambda|\ge a_k}\lambda P_\lambda=TR_k.
\]
The contractivity of \(R_k\) gives
\[
\|TR_k\|\le a_{k+1}.
\]
The reverse inequality follows by evaluating \(TR_k\) on a unit eigenvector whose eigenvalue has modulus \(a_{k+1}\). Thus
\[
\left\|T-\sum_{|\lambda|\ge a_k}\lambda P_\lambda\right\|
=a_{k+1}.
\]
If there is no next nonzero spectral value, then \(r(T_k)=0\), hence
\(\|T_k\|=0\), so the remainder is zero.

Since \(a_k\to0\) for an infinite compact spectrum, the spectral expansion converges in operator norm.

### 6. Uniform control for a one-eigenvalue-at-a-time extraction

At a fixed modulus \(a\), the real spectrum contains at most the pair
\(\{a,-a\}\). In a norm-greedy extraction, all larger modulus levels have already been completely removed, and at most one member of the current sign pair has been removed.

Let \(Q_{>a}\) be the projection onto all eigenspaces with modulus strictly larger than \(a\). Step 4 gives
\[
\|Q_{>a}\|\le2.
\]
If one member \(\lambda\in\{a,-a\}\) has additionally been removed, Step 3 gives
\[
\|Q_{>a}+P_\lambda\|\le3.
\]
Thus all partial spectral projections arising from the norm-greedy extraction are uniformly bounded by \(3\); their complementary residual projections are bounded by \(4\).

For the remainder itself one gets a sharper estimate. If a modulus block is complete, Step 5 gives exact norm equal to the next modulus. If only one member of a sign pair has been removed, the remainder is the other term, of norm exactly \(a\), plus the completed-block tail, whose norm is at most \(a\). Hence
\[
\|T-S_n\|\le2\rho_n,
\]
where \(\rho_n\) is the largest omitted modulus. Compactness gives \(\rho_n\to0\).

## Relation to recent literature

Shameem and Deepesh, arXiv:2608.06873v1, state an operator-norm spectral representation theorem for compact operators satisfying this duality-self-adjointness condition. A detailed public review of that version identifies an unproved final estimate: the proof treats the residual projection as contractive, although arbitrary Auerbach residual projections in a smooth Banach space need not be contractive.

The argument above separates the two issues. Arbitrary Auerbach residuals indeed need not be contractive. For the residuals generated by an actual compact duality-self-adjoint operator, however, invariant spectral structure supplies extra information. After complete modulus blocks the spectral gap forces the residual projection to be contractive; individual nonzero Riesz projections are themselves contractive; and a possible \(+a/-a\) tie costs only a uniformly bounded intermediate step. This supplies an operator-norm convergence proof and in fact gives exact tail norms at completed modulus levels.

The normalized duality-map conventions and its conjugate homogeneity on smooth complex Banach spaces agree with García-Pacheco's treatment. The identity \(r(T)=\|T\|\) for this self-adjoint class is also consistent with the 2026 work of Shameem and Deepesh; it is reproved above directly so that the tail estimate does not depend on an imported norm-attainment theorem.

## Limitations

The result concerns the specific duality-map notion of self-adjointness \(T^*J=JT\), not arbitrary Hermitian operators under other Banach-space definitions.

The exact tail formula is naturally stated after completing all eigenvalues of a given modulus. A partial block can occur only when both \(a\) and \(-a\) are eigenvalues; for such an intermediate step the record gives the uniform \(2a\) remainder bound rather than an exact formula.

The primary arXiv abstract for 2608.06873v1 was inspected, while theorem-level details of its proof and the reported projection gap were available through detailed public secondary renderings rather than a directly inspected primary full text. This does not affect the self-contained proof above, but it leaves some uncertainty about the exact wording of the source proof. The 2020 paper by García-Pacheco on selfadjoint operators was located and its abstract inspected, but its full text was not inspected; it is the most plausible older source that could contain part of the projection mechanism under different terminology.

Originality is therefore claimed only to the best of our knowledge for the spectral-gap contractivity mechanism, contractivity of the nonzero Riesz projections in this setting, the exact modulus-block tail norm, and their use to close the reported convergence gap.

## References

1. M. Shameem and D. K. P., *Spectral theorem for compact self-adjoint operators on smooth Banach spaces*, arXiv:2608.06873v1 (2026). https://arxiv.org/abs/2608.06873
2. Pith, review of arXiv:2608.06873, including the reported residual-projection gap. https://www.pith.science/paper/2608.06873
3. F. J. García-Pacheco, *The adjoint of an operator on a Banach space*, Collectanea Mathematica 75 (2024), 823--840. https://doi.org/10.1007/s13348-023-00414-8
4. F. J. García-Pacheco, *Selfadjoint operators on real or complex Banach spaces*, Nonlinear Analysis 192 (2020), 111696. https://doi.org/10.1016/j.na.2019.111696
5. M. Shameem and D. K. P., *On properties of normal operators and self-adjoint operators on smooth Banach spaces*, arXiv:2605.15898v1 (2026). https://arxiv.org/abs/2605.15898
