# A sharp cubic-zero Embry-moment gap and a cubic-power stability law

## Finding
Let \(H\) be any real or complex Hilbert space, and \(T\in\mathcal B(H)\) be nonzero. Define the second operator-moment discrepancy
\[
\Delta(T)=\left\|(T^*T)^2-(T^2)^*T^2\right\|,
\qquad \varepsilon(T)=\frac{\|T^3\|}{\|T\|^3}\in[0,1].
\]
Then the dimension-free cubic-power stability estimate is
\[
\boxed{\frac{\Delta(T)}{\|T\|^4}\ge\frac{3-\sqrt{5+4\varepsilon(T)^2}}{2}.}
\]
In particular, for every nonzero cubic-zero operator \(T^3=0\),
\[
\boxed{\Delta(T)\ge\frac{3-\sqrt5}{2}\|T\|^4,}
\]
and the numerical constant is the largest universally valid one. It is attained on a three-dimensional Hilbert space. The endpoint of the envelope at \(\varepsilon=1\) is also sharp. We do not assert pointwise optimality of the envelope for intermediate \(0<\varepsilon<1\).

## Assumptions and scope
Every bounded nonzero operator on a real or complex Hilbert space of arbitrary dimension is included, whether norm-attaining or not; no normality, positivity, compactness or finite-rank assumption is imposed. The term *cubic-zero* means \(T^3=0\), with \(T^2\) permitted to be nonzero. The norm is the operator norm. Both summands inside \(\Delta(T)\) are bounded self-adjoint positive operators, although their difference need not be positive. Scaling by a nonzero scalar multiplies \(\Delta\) by the fourth power of its absolute value.

## Proof
By homogeneity, normalize \(\|T\|=1\). Set \(A=T^*T\), \(D=A^2-(T^2)^*T^2\), \(\delta=\|D\|\) and \(\varepsilon=\|T^3\|\). For every unit vector \(x\), write
\[
a=\|Tx\|^2,\qquad b=\|T^2x\|^2,\qquad c=\|T^3x\|^2.
\]
Thus \(0\le a,b,c\le1\). Cauchy–Schwarz implies \(\|Ax\|^2\ge\langle Ax,x\rangle^2=a^2\), hence
\[
\delta\ge\langle Dx,x\rangle=\|Ax\|^2-b\ge a^2-b.\tag{1}
\]
Whenever \(a>0\), the unit vector \(y=Tx/\sqrt a\) satisfies \(\|Ty\|^2=b/a\) and \(\|T^2y\|^2=c/a\). Apply (1) to \(y\):
\[
\delta\ge\frac{b^2}{a^2}-\frac ca\ge\frac{b^2}{a^2}-\frac{\varepsilon^2}{a}.\tag{2}
\]
Choose a sequence of unit vectors \(x_j\) with \(a_j=\|Tx_j\|^2\to1\). Extract a subsequence along which \(b_j=\|T^2x_j\|^2\to t\in[0,1]\). Passing to the limit in (1) and (2) gives
\[
\delta\ge \max\{1-t,\ t^2-\varepsilon^2\}.
\]
The first term decreases and the second increases on \([0,1]\). They intersect at the unique root
\[
t_* =\frac{\sqrt{5+4\varepsilon^2}-1}{2}\in[0,1]
\]
of \(1-t=t^2-\varepsilon^2\). Consequently
\[
\delta\ge1-t_*=\frac{3-\sqrt{5+4\varepsilon^2}}2.
\]
Undo homogeneity to prove the general estimate, including operators whose norms are not attained.

For exact sharpness at cubic zero, put \(\tau=(\sqrt5-1)/2\), and in the standard orthonormal basis of \(\mathbb C^3\) set \(Te_1=e_2\), \(Te_2=\sqrt\tau\,e_3\), \(Te_3=0\). Then \(\|T\|=1\), \(T^3=0\), and direct multiplication yields
\[
(T^*T)^2-(T^2)^*T^2=\operatorname{diag}(1-\tau,\tau^2,0).
\]
Since \(1-\tau=\tau^2=(3-\sqrt5)/2\), equality holds. The same real matrix gives sharpness on real Hilbert spaces. At the other endpoint, \(T=I\) has \(\varepsilon=1\) and \(\Delta(I)=0\), giving equality there too.

## Verification
The proof is analytic and needs no spectral approximation or norm attainment. To reproduce the finite diagnostics, run `python verify.py` in an environment with NumPy. The script verifies the exact three-dimensional sharp configuration numerically and tests 7,403 finite assertions, including generic complex matrices and arbitrary three-layer nilpotent block matrices. The random tests are supplementary and do not certify the infinite-dimensional theorem. The exact constant follows algebraically from \(\tau^2+\tau=1\).

## Relationship to prior work
Embry-type conditions compare \((T^*T)^k\) and \((T^k)^*T^k\). Pietrzycki's 2026 work proves qualitative quasinormality from two separate exact moment equalities; Pietrzycki and Stochel give related quasinormality equivalences. These are not statements of a *sharp positive operator-norm discrepancy* on the cubic-zero class. The latter is a natural first nilpotent class in which the second iterate need not vanish, and hence where competing second moments can nearly cancel. The present theorem concerns one sharp quantitative fourth-degree defect and a general cubic-power stability envelope, not a converse or substitute for the prior all-exponent classification.

## Limitations
The parameter-dependent estimate is proved universally but is claimed sharp only at \(\varepsilon=0\) and \(\varepsilon=1\). No equality classification for all operators is claimed. A recent potentially related source was accessible by abstract, not full text; complete historical priority remains to be checked independently. Nothing here proves an all-operator quantitative distance-to-quasinormality theorem.

## References
1. Paweł Pietrzycki, “Reduced Embry characterizations of quasinormal operators”, arXiv:2610.17303, first publicly submitted 2026-10-12, https://arxiv.org/abs/2610.17303.
2. Paweł Pietrzycki and Jan Stochel, “On nth roots of bounded and unbounded quasinormal operators”, *Annali di Matematica Pura ed Applicata* 202 (2023), 1313–1333, DOI:10.1007/s10231-022-01281-z (first online 2022). See Theorems 2.1 and 4.1.
