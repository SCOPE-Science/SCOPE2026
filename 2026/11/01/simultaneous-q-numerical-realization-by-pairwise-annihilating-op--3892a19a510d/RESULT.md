# Simultaneous \(q\)-numerical realization by pairwise-annihilating operator families

## Finding

Let \(\Omega\) be a nonempty compact Hausdorff space and let \(K\subset C(\Omega;\mathbb C)\) be a nonempty **norm-compact, absolutely convex** set (that is, a closed complex-balanced convex set). There is one complex Hilbert space \(H\) and one norm-continuous family \(F:\Omega\to\mathcal B(H)\) such that

\[
F(s)F(t)=0\quad(s,t\in\Omega),\qquad
\sup_{s\in\Omega}\|F(s)\|=\max_{f\in K}\|f\|_\infty,
\]

and, **simultaneously for every** \(q\in\mathbb C\) with \(|q|\le1\),

\[
\boxed{\mathcal W_q(F)=c(|q|)K,\qquad
c(\rho)=\frac{1+\sqrt{1-\rho^2}}2.}
\]

Here \(\mathcal W_q(F)\) is the set of functions \(s\mapsto\langle F(s)x,y\rangle\) with \(\|x\|=\|y\|=1\) and \(\langle x,y\rangle=q\). The family can be chosen to consist of mutually annihilating square-zero operators (all of whose products, not merely squares, vanish). The coefficient \(c(\rho)\) is the exact optimal coefficient budget for a norm-one square-zero operator. Rescaling the **same family** by two gives a realization equal to \(K\) at \(|q|=1\) and equal to \((1+\sqrt{1-|q|^2})K\) at every other admissible parameter.

## Assumptions and scope

The inner product is complex-linear in its first variable. The symbol \(C(\Omega;\mathbb C)\) is equipped with the supremum norm. Absolute convexity means that \(\sum_{j=1}^r\alpha_j f_j\in K\) whenever \(f_j\in K\) and \(\sum_j|\alpha_j|\le1\); equivalently, \(K\) is convex and invariant under all scalars of modulus at most one. In particular \(0\in K\). The index set \(K\) need not be countable and no separability of \(H\) is asserted. A nonempty compact domain is assumed to avoid empty-domain conventions. The result covers the full closed complex parameter disk, including \(q=0\) and \(|q|=1\).

## Proof

**1. Sharp square-zero estimate.** Let \(T\in\mathcal B(H)\) satisfy \(\|T\|\le1\) and \(T^2=0\). For unit vectors \(x,y\) with \(\langle x,y\rangle=q\), write \(\rho=|q|\) and \(r=\sqrt{1-\rho^2}\). Since \(T^2=0\), \(T\) vanishes on its kernel and maps \((\ker T)^\perp\) into \(\ker T\). Put \(t=\|P_{(\ker T)^\perp}x\|^2\) and \(z=|\langle Tx,x\rangle|\). Then

\[
0\le z\le\sqrt{t(1-t)},\qquad \|Tx\|\le\sqrt t.
\]

Decomposing \(y\) into its component along \(x\) and an orthogonal unit vector, and using Cauchy--Schwarz on the orthogonal component of \(Tx\), gives

\[
|\langle Tx,y\rangle|\le \rho z+r\sqrt{t-z^2}.
\]

For \(t\le r^2\), its unconstrained maximum in \(z\) is \(\sqrt t\le r\le(1+r)/2\). For \(t\ge r^2\), the maximizer on \([0,\sqrt{t(1-t)}]\) is the upper endpoint, and hence

\[
|\langle Tx,y\rangle|
\le \rho\sqrt{t(1-t)}+rt
\le \frac{1+r}{2}.
\]

The last inequality is the largest-eigenvalue formula for the real symmetric matrix \(\begin{psmallmatrix}0&\rho/2\\\rho/2&r\end{psmallmatrix}\). The same calculation covers the endpoint cases \(\rho=0,1\). Optimality holds for the matrix \(N=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\). For \(0\le\rho\le1\), set \(t=(1+r)/2\), \(x=(\sqrt{1-t},\sqrt t)\), \(w=(\sqrt t,-\sqrt{1-t})\), and \(y=\rho x+rw\). Then \(x,y\) are unit, \(\langle x,y\rangle=\rho\), and \(\langle Nx,y\rangle=(1+r)/2\). Multiplication of the second vector by a phase handles nonreal \(q\). This is a sharp estimate for all square-zero contractions, not an assertion that the scalar estimate was previously unknown.

**2. One explicit continuous family.** Set \(E=\ell_2(K)\) with orthonormal basis \((e_f)_{f\in K}\), and \(H=E\oplus E\). For \(s\in\Omega\) define the diagonal operator \(D(s)e_f=f(s)e_f\) and the block operator

\[
F(s)=\begin{pmatrix}0&D(s)\\0&0\end{pmatrix}.
\]

The norm-compactness of \(K\) implies that its elements are uniformly equicontinuous at every point: a finite supremum-norm net controls the pointwise oscillation of every member. Thus

\[
\|D(s)-D(t)\|=\sup_{f\in K}|f(s)-f(t)|\longrightarrow0\quad(t\to s).
\]

Therefore \(F\) is norm-continuous. Direct block multiplication shows \(F(s)F(t)=0\) for all parameters. Moreover \(\|F(s)\|=\sup_{f\in K}|f(s)|\), giving the stated sup norm.

**3. The upper inclusion.** Write unit vectors as \(x=(u,v)\), \(y=(a,b)\) in \(E\oplus E\), with \(\langle x,y\rangle=q\). Their output function is

\[
\langle F(\cdot)x,y\rangle=\sum_{f\in K}\alpha_f f,
\qquad \alpha_f=v_f\overline{a_f}.
\]

Only countably many coefficients are nonzero and the series converges absolutely in the supremum norm. Choose a diagonal unitary \(U\) on \(E\) with diagonal phases that align the nonzero numbers \(\alpha_f\). The block operator \(T_U=\begin{psmallmatrix}0&U\\0&0\end{psmallmatrix}\) is a square-zero norm-one operator, and

\[
\sum_{f\in K}|\alpha_f|=|\langle T_Ux,y\rangle|\le c(|q|).
\]

Absolute convexity puts each finite partial sum in \(c(|q|)K\); this set is norm-closed, so the entire sum belongs to it. Thus \(\mathcal W_q(F)\subset c(|q|)K\).

**4. The lower inclusion for all complex phases.** Fix \(f\in K\). The two-dimensional reducing coordinate block associated with \(e_f\) carries \(F(s)=f(s)N\). The explicit pair in Step 1 therefore produces exactly the function \(c(\rho)f\) when \(q=\rho\in[0,1]\). This proves \(c(\rho)K\subset\mathcal W_\rho(F)\). If \(q=\rho e^{i\theta}\), multiplying the second unit vector by \(e^{-i\theta}\) changes the overlap from \(\rho\) to \(q\) and multiplies every output by \(e^{i\theta}\). Hence \(\mathcal W_q(F)=e^{i\theta}\mathcal W_\rho(F)\), which equals \(c(\rho)K\) because \(K\) is complex-balanced. The same reasoning applies at \(q=0\). This proves both inclusions and the simultaneous statement.

## Verification

The standalone file `VERIFY.py` checks finite-dimensional instances of the block construction, all cross-products, operator norms, complex \(q\)-constraints, absolute-coefficient budgets, and exact two-coordinate witnesses. It reported **35,789 passed deterministic assertions**, using Python and NumPy. These tests are corroborative; the proof above establishes the arbitrary-dimensional and all-parameter assertions.

## Relationship to prior work

Azadi, *Joint \(q\)-Numerical Ranges of Continuous Operator-Valued Functions* (arXiv:2610.32504, first submitted 2026-10-23), Theorem 2.16, constructs a realization at **\(|q|=1\)**, using diagonal multiplication. That result does not provide the same family across all \(|q|<1\) or the mutual-annihilation constraint. Feki--Patra--Rani--Taki (arXiv:2410.03669) study joint \(q\)-ranges of operator tuples but do not give this simultaneous function-valued realization. Denčić--Stanković--Krstić--Damnjanović (arXiv:2503.05036) establish a general single-rank-one \(q\)-numerical radius formula: the scalar sharp radius of \(N\) is prior context, not the claimed innovation. The contribution is the combination of exact shape realization for arbitrary compact absolutely convex function sets, one fixed operator family for all \(q\), preserved sup norm, and pairwise vanishing products.

## Limitations

The target set is required to be compact and absolutely convex; this theorem does not realize arbitrary nonbalanced convex sets for \(|q|<1\). Complex balance is not merely a proof convenience: for any operator family, every point of \(\mathcal W_0(F)\) carries its whole unimodular orbit, so a nonbalanced target cannot equal the zero-parameter range. The construction may require a nonseparable Hilbert space. It proves set equality and an optimal square-zero coefficient, but neither a minimal Hilbert-space dimension nor geometric stability of nearby realizations. An earlier equivalent universal-realization construction under different terminology would affect publication priority; no independent publication-priority certification has been performed.

## References

1. A. Azadi, *Joint \(q\)-Numerical Ranges of Continuous Operator-Valued Functions*, arXiv:2610.32504 (first submitted 2026-10-23), Theorem 2.16. https://arxiv.org/abs/2610.32504
2. K. Feki, A. Patra, J. Rani, Z. Taki, *Joint \(q\)-Numerical Ranges of Operators in Hilbert and Semi-Hilbert Spaces*, arXiv:2410.03669 (first submitted 2024-09-12). https://arxiv.org/abs/2410.03669
3. D. Denčić, H. Stanković, M. Krstić, I. Damnjanović, *\(q\)-numerical radius of rank-one operators and the generalized Buzano inequality*, arXiv:2503.05036 (first submitted 2025-03-06). https://arxiv.org/abs/2503.05036
4. M. Abtahi and A. Azadi, *Joint numerical ranges of continuous operator-valued functions*, Acta Sci. Math. (Szeged) (2025), DOI:10.1007/s44146-025-00218-1.
