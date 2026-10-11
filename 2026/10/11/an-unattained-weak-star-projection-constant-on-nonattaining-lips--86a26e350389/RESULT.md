# An unattained weak-star projection constant on nonattaining Lipschitz subspaces

## Finding

Let \(M\) be an infinite equilateral metric space with \(|M|=\kappa\) and fix any basepoint. Normalize its positive common nonzero distance to \(1\), and give \(X=\operatorname{Lip}_0(M;\mathbb R)=\mathcal F(M)^*\) the canonical weak-star topology induced by its Lipschitz-free predual. There is a **weak-star closed**, linearly isometric copy \(Y\) of \(\ell_\infty(\kappa)\) in \(X\) such that every \(y\in Y\setminus\{0\}\) fails both pointwise Lipschitz-norm attainment and norm attainment as a functional on \(\mathcal F(M)\). For the same \(Y\),
\[
\inf\big\{\|P\|:\ P:X\to Y\text{ is a weak-star continuous linear projection}\big\}=1,
\]
but the infimum is **not attained**. Explicit weak-star continuous projections satisfy \(\|P_k\|=(k+1)/k\) for all \(k\ge1\), while an ordinary bounded projection \(P_0:X\to Y\) satisfies \(\|P_0\|=1\) and is necessarily not weak-star continuous.

## Assumptions and scope

All scalars are real, and \(M\) is infinite with \(d(p,q)=1\) for all distinct \(p,q\). For \(f\in X\), the Lipschitz norm is its value-range diameter. A function is pointwise norm attaining if there is a fixed \(p\) for which the supremum of its slopes from \(p\) equals its global Lipschitz norm. A functional \(f\in\mathcal F(M)^*\) is norm attaining if it attains its operator norm on some unit vector of \(\mathcal F(M)\). The weak-star topology on \(X\) is \(\sigma(X,\mathcal F(M))\). The theorem concerns the specified subspace \(Y\), not the class of every possible isometric copy.

Choose a bijection \(M\cong\Gamma\times\mathbb N\times\{-1,+1\}\) with \(|\Gamma|=\kappa\) and let \(o=(\gamma_0,k_0,s_0)\) be the basepoint. Write \(r_k=k/(k+1)\in(0,1)\).

## Proof

**The sign-paired embedding and its nonattainment.** For \(a\in\ell_\infty(\Gamma)\), define \(u_a(\gamma,k,s)=s r_k a_\gamma/2\) and \(T(a)(p)=u_a(p)-u_a(o)\). Let \(A=\|a\|_\infty\). Since both signs occur and \(r_k\uparrow1\), the values of \(u_a\) have supremum \(A/2\) and infimum \(-A/2\), neither attained when \(a\ne0\). Consequently \(\|T(a)\|_{\mathrm{Lip}}=A\), so \(T\) is a linear isometry with closed range \(Y\). At the point \(p=(\gamma,k,s)\),
\[
\sup_{q\ne p}\frac{|T(a)(q)-T(a)(p)|}{d(p,q)}
=\frac{A+r_k|a_\gamma|}{2}<A
\qquad (a\ne0),
\]
which excludes all nonzero image functions from pointwise norm attainment.

**The predual nonattainment lemma.** For an equilateral metric, \(\mathcal F(M)\) is isometric to the zero-sum subspace \(\ell_1^0(M)=\{\mu\in\ell_1(M):\sum_{p\in M}\mu_p=0\}\), with norm \(\|\mu\|_{\mathcal F}=\tfrac12\sum_p|\mu_p|\). To see this, move the positive mass of each finitely supported zero-sum signed measure to its negative mass; cost equals the common positive mass, and the test function taking value \(1\) on the positive support and \(0\) on the negative support provides the matching dual lower bound. Complete in \(\ell_1\). For \(\|\mu\|_{\mathcal F}=1\), both the positive and negative parts have total mass \(1\). If \(f\) has range extrema \(\alpha=\inf_M f\) and \(\beta=\sup_M f\), and neither extremum is attained, then
\[
\langle f,\mu\rangle
=\sum_p f(p)\mu_p^+-\sum_p f(p)\mu_p^-<\beta-\alpha=\|f\|_{\mathrm{Lip}}.
\]
The inequality is strict because both nonzero mass components occur on points strictly inside \((\alpha,\beta)\). Applying the same argument to \(-\mu\) gives \(|\langle f,\mu\rangle|<\|f\|_{\mathrm{Lip}}\). Therefore every nonzero \(T(a)\) also fails functional norm attainment on \(\mathcal F(M)\).

**Weak-star closure.** Define the coordinate \(b_\gamma(f)=[f(\gamma,1,+1)-f(\gamma,1,-1)]/r_1\). It is a weak-star continuous functional on \(X\), and \(\|b(f)\|_\infty\le\|f\|_{\mathrm{Lip}}/r_1\). One has \(f\in Y\) if and only if, for every \(p=(\gamma,k,s)\),
\[
f(p)=\frac{s r_k b_\gamma(f)-s_0r_{k_0}b_{\gamma_0}(f)}2.
\]
Indeed necessity follows from the definition of \(T\), and sufficiency follows by taking \(a=b(f)\). Each equality involves finitely many point evaluations, which are weak-star continuous. Their common solution space \(Y\) is therefore weak-star closed.

**An unattained weak-star projection infimum.** For each integer \(k\ge1\), set
\[
Q_k(f)_\gamma=\frac{f(\gamma,k,+1)-f(\gamma,k,-1)}{r_k},
\qquad P_k=TQ_k.
\]
Every coordinate of \(Q_k\) is a scaled molecule evaluation, so \(Q_k:X\to\ell_\infty(\Gamma)\) is weak-star continuous for the canonical predual \(\ell_1(\Gamma)\); \(T\) is weak-star continuous because each output evaluation depends on finitely many coordinates. As \(Q_kT=I\), \(P_k\) is a weak-star continuous projection onto \(Y\). Its norm is **exactly** \(1/r_k=(k+1)/k\): the pairwise Lipschitz bound gives \(\|Q_k\|\le1/r_k\), while the indicator function of the positive member of a selected sign-pair has Lipschitz norm \(1\) and gives one coordinate of \(Q_k\) value \(1/r_k\). Since \(T\) is an isometry, \(\|P_k\|=\|Q_k\|\). These norms converge to \(1\), and any nonzero projection has norm at least \(1\).

Suppose that a weak-star continuous projection \(P:X\to Y\) had norm \(1\). Choose \(\gamma\in\Gamma\) and the standard unit vector \(e_\gamma\in\ell_\infty(\Gamma)\). The coefficient functional \(c_\gamma:Y\to\mathbb R\), \(c_\gamma(Ta)=a_\gamma\), has norm \(1\). Thus \(c_\gamma P\) is a weak-star continuous linear functional on \(X\) of norm at most \(1\), hence evaluation by some \(\mu\in\mathcal F(M)\) with \(\|\mu\|\le1\). But
\[
\langle T(e_\gamma),\mu\rangle=(c_\gamma P)(T(e_\gamma))=1
=\|T(e_\gamma)\|_{\mathrm{Lip}},
\]
contradicting the predual nonattainment lemma. Therefore no weak-star continuous norm-one projection onto \(Y\) exists.

**An ordinary norm-one projection.** The usual limit on convergent real sequences has norm \(1\). Extend it by Hahn--Banach to a norm-one \(\Lambda\in\ell_\infty(\mathbb N)^*\). Put \(Q_0(f)_\gamma=\Lambda((f(\gamma,k,+1)-f(\gamma,k,-1))_k)\). Partner differences have modulus at most \(\|f\|_{\mathrm{Lip}}\), so \(\|Q_0\|\le1\); because \(r_k\to1\), \(Q_0T=I\). Hence \(P_0=TQ_0\) is a projection onto \(Y\) of norm exactly \(1\), and the previous argument shows it cannot be weak-star continuous. This completes the single stated projection-gap phenomenon.

## Verification

All infinite-dimensional claims are proved above by exact identities, the \(\ell_1^0\) predual model, weak-star point evaluations, and Hahn--Banach. The supplemental `verify.py` carries out rational finite-section tests of the sign-paired norm, strict pointwise deficits and weak-star projection-level constants for \(k=1,\ldots,5\). It cannot verify the infinite supremum or an infinite weak-star nonattainment statement; those are analytic, not computational, claims. Run `python3 verify.py` with the Python standard library.

## Relationship to prior work

Choi--Jung--Lee--Roldán (2023, arXiv:2312.00393v1, Definition 2.1 and Example 2.2) **already prove** the characterization of pointwise norm attainment on infinite equilateral metrics in terms of attainment of a range extremum. This known criterion is input, not a new finding. Choi--Jung--Lee--Roldán (2024, arXiv:2404.07599v1, Lemma 2.1, Theorem 2.2 and Proposition 4.2) give isometric \(\ell_\infty\) families of nonattainers, including failure of functional norm attainment for arbitrary infinite metrics and pointwise nonattainment on Banach-space domains. Their inspected statements do not determine weak-star continuous projection constants onto such an image. In contrast, the present theorem establishes a **weak-star closed** nonattaining \(\ell_\infty(\kappa)\) range with an **unattained sharp weak-star projection infimum** and a **realized ordinary projection infimum**.

## Limitations

The result is for real-valued functions on equilateral infinite metrics and the particular embedded copy \(Y\), not arbitrary metric spaces or all embedded copies. The ordinary norm-one projection uses a noncanonical Hahn--Banach extension and is not weak-star continuous. Finite computations do not certify weak-star topology or infinite-dimensional nonattainment. No claim is made about the existence of a unique projection or about universal priority.

## References

1. G. Choi, M. Jung, H. J. Lee, Ó. Roldán, *Embeddings of infinite-dimensional spaces in the sets of norm-attaining Lipschitz functions*, arXiv:2312.00393v1 (2023-12-01), Definition 2.1 and Example 2.2. https://arxiv.org/abs/2312.00393
2. G. Choi, M. Jung, H. J. Lee, Ó. Roldán, *Linear structures of norm-attaining Lipschitz functions and their complements*, arXiv:2404.07599v1 (2024-04-11), Lemma 2.1, Theorem 2.2, Proposition 4.2. https://arxiv.org/abs/2404.07599
