# A sharp one-coordinate retention threshold for PSD truncated power iteration

## Finding
For every integer \(m\ge 2\), number \(n\ge m+1\), and \(0<q<1\), let \(A\in\mathbb R^{n\times n}\) be symmetric positive semidefinite with a simple top eigenvalue \(1\), top eigenvector \(e_1\), and remaining eigenvalues in \([0,q]\). Let \(H_m\) retain the \(m\) coordinates of largest absolute value, with arbitrary decisions at ties, and define the normalized truncated power iteration \(x_{t+1}=H_m(Ax_t)/\|H_m(Ax_t)\|_2\) from any unit vector \(x_0\) with at most \(m\) nonzeros and \(a=|\langle e_1,x_0\rangle|>0\).

The sharp universal **coordinate-retention** threshold is
\[
\tau_m(q)=\frac{q^2(m-1)}{m^2+q^2(m-1)}.
\]
If \(a^2>\tau_m(q)\), the first coordinate is retained at every iteration, regardless of ties, and
\[
|\langle e_1,x_t\rangle|^2\ge\frac{1}{1+q^{2t}(1-a^2)/a^2},\qquad
0\le 1-x_t^\top A x_t\le\frac{q^{2t}(1-a^2)}{a^2+q^{2t}(1-a^2)}.
\]
In particular, the iterates converge to the top eigendirection at least geometrically. Conversely, for every \(a^2<\tau_m(q)\), an explicit rank-one-tail positive semidefinite matrix ejects the first coordinate in a single step and traps every later iterate at Rayleigh quotient \(q\). At equality, an admissible tie decision also ejects it. Thus the strict threshold is optimal for a guarantee independent of tie handling.

## Assumptions and scope
All matrices and vectors are real. The top eigencoordinate is exactly one-sparse, the top eigenvalue is normalized to one, the other eigenvalues are nonnegative and at most \(q<1\), and the starting vector is already at most \(m\)-sparse. The result is independent of ambient dimension \(n\ge m+1\). Here \(H_m\) selects exactly \(m\) coordinate positions, including possible zeros, so no artificially chosen rule at a tie is presumed. The denominator in the iteration is nonzero in the retaining regime because its first component is nonzero, and is nonzero in every counterexample below.

## Proof
**A positive-semidefinite order-statistic lemma.** Let \(B\) be real symmetric with \(0\preceq B\preceq qI\), and let \(z\) have support \(S\) of size at most \(m-1\). Write \(w=Bz\). The \(m\)-th largest number among the absolute coordinates of \(w\) satisfies
\[
|w|_{(m)}\le\frac{q\sqrt{m-1}}{m}\,\|z\|_2. \tag{1}
\]
To prove this, by homogeneity take \(\|z\|_2=1\). If the order statistic is zero the claim is immediate. Otherwise let \(T\) index \(m\) coordinates of absolute magnitude at least \(h=|w|_{(m)}>0\), let \(k=|S\cap T|\le m-1\), and put \(r=\|w_S\|_2\). Then \(r\ge\sqrt{k}\,h\), and the disjoint coordinates in \(T\setminus S\) show \(\|w\|_2^2\ge r^2+(m-k)h^2\). Since \(B^2\preceq qB\),
\[
r^2+(m-k)h^2\le\langle z,B^2z\rangle\le q\langle z,Bz\rangle\le qr.
\]
Consequently, with \(s=r/h\ge\sqrt k\), \(h\le q s/(s^2+m-k)\). If \(2k\le m\), the maximum over \(s\ge\sqrt k\) is \(q/(2\sqrt{m-k})\), which is at most \(q\sqrt{m-1}/m\). To see the latter inequality, \(m^2\le 4(m-k)(m-1)\) for \(2k\le m\), \(m\ge2\); indeed it suffices to use \(m-k\ge m/2\) and \(m^2\le 2m(m-1)\). If \(2k>m\), this maximum is attained at \(s=\sqrt k\) and equals \(q\sqrt k/m\le q\sqrt{m-1}/m\). This proves (1). Its constant is attained by \(B=(q/m)\mathbf1\mathbf1^\top\) on an \(m\)-coordinate block and \(z=(1,\ldots,1,0)^\top/\sqrt{m-1}\) in that block.

**Retention and convergence.** The spectral hypotheses and \(Ae_1=e_1\) imply the orthogonal block decomposition \(A=\operatorname{diag}(1,B)\) with \(0\preceq B\preceq qI\). Write \(x_t=(a_t,z_t)\), where \(a_t\) may carry a sign, \(\|x_t\|_2=1\), and \(z_t\) has at most \(m-1\) nonzero coordinates whenever the first coordinate was retained previously. The first entry of \(Ax_t\) has magnitude \(|a_t|\). Applying (1) to the tail yields \(|(Bz_t)|_{(m)}\le (q\sqrt{m-1}/m)\|z_t\|_2\). Since \(|a_0|^2>\tau_m(q)\) is precisely \(|a_0|>(q\sqrt{m-1}/m)\sqrt{1-|a_0|^2}\), the leading coordinate is strictly above the competing \(m\)-th tail coordinate. It therefore belongs to every top-\(m\) selection. It is unchanged before normalization, while the tail norm can only shrink relative to multiplication by \(B\): with \(z_t'\) the truncated unnormalized tail,
\[
\|z_t'\|_2\le\|Bz_t\|_2\le q\|z_t\|_2.
\]
After renormalization the tail-to-leading ratio \(r_t=\|z_t\|_2/|a_t|\) obeys \(r_{t+1}\le qr_t\). In particular, \(|a_t|\) never decreases, so the strict threshold persists. Induction gives \(r_t\le q^t\sqrt{1-a^2}/a\), the displayed overlap bound, and convergence to the top eigendirection. Finally \(x_t^\top A x_t=|a_t|^2+z_t^\top Bz_t\ge |a_t|^2\); the upper bound follows.

**Sharpness, including the tie boundary.** Take \(n=m+1\), \(A=\operatorname{diag}(1,(q/m)\mathbf1_m\mathbf1_m^\top)\), and choose \(x_0=(a,\sqrt{1-a^2}\,u_0)\), where \(u_0\in\mathbb R^m\) has its first \(m-1\) entries equal to \(1/\sqrt{m-1}\) and its last entry zero. The first input has exactly \(m\) nonzeros. The transformed tail has all \(m\) coordinates equal to \(q\sqrt{(m-1)(1-a^2)}/m\), while its leading coordinate is \(a\). If \(a^2<\tau_m(q)\), all \(m\) tail coordinates strictly dominate \(a\), so truncation deletes the leading coordinate. If \(a^2=\tau_m(q)\), a tie decision can delete it. Normalization then gives \(x_1=(0,u)\), where \(u=\mathbf1_m/\sqrt m\) is an eigenvector of the tail with eigenvalue \(q\). Since \(H_m(Ax_1)=qx_1\), every subsequent iterate is \(x_1\) and has Rayleigh quotient \(q<1\). No uniformly weaker overlap condition can force support retention for all admissible inputs.

## Verification
A standalone Python checker `verify.py` uses exact rational arithmetic to demonstrate both sides of the threshold for \(m\in\{2,3,4,5,8,13\}\) and \(q\in\{1/4,1/2,3/4\}\). It additionally samples seeded positive semidefinite matrices satisfying the hypotheses to test the retention bound and update behavior. Running `python verify.py` produces the recorded `verify_output.txt`. These finite tests are a reproducibility supplement; the argument above establishes the all-dimension theorem.

## Relationship to prior work
Hajlasz, Musco, Weare and Webber (2026), arXiv:2610.14620v1, give a dimension-independent sparsified-power approximation guarantee under eigenvector compressibility and a sufficient truncation-budget condition. Their arguments do not give the exact tie-independent overlap threshold for an exactly one-coordinate top eigenvector or a matching permanently trapped positive semidefinite counterexample. Yuan and Zhang (2013) introduce the truncated power method and prove convergence/recovery statements under perturbation hypotheses; their sufficient conditions are not this sharp global overlap dichotomy on the one-coordinate model. The present statement specializes to the mathematically natural exact-sparsity boundary and addresses the otherwise uncontrolled possibility that a power multiplication erases its unique desired eigencoordinate. It neither improves every parameter regime of the two broader theories nor claims that the classical algorithm is new.

## Limitations
The result assumes an exactly one-coordinate dominant eigenvector, a positive semidefinite tail, an at-most-\(m\)-sparse start, and \(m\ge2\). It does not extend as stated to signed-indefinite tails, non-sparse starts, approximate leading support, or noisy eigenspaces. At equality, retention depends on tie-breaking. The convergence bound controls an idealized exact-arithmetic iteration and is not a roundoff stability theorem. Existing sparse PCA or hard-thresholding literature may use equivalent support-preservation terminology; this remains an originality risk pending independent review.

## References
1. Hajlasz, Musco, Weare and Webber, *Dimension-independent eigenvalue approximation for sparse matrices*, arXiv:2610.14620v1 (first public version 2026-10-10), https://arxiv.org/abs/2610.14620.
2. X.-T. Yuan and T. Zhang, *Truncated Power Method for Sparse Eigenvalue Problems*, Journal of Machine Learning Research **14** (2013), 899–925, https://www.jmlr.org/papers/v14/yuan13a.html.
