# Exact residual-vacancy law for competing dimers and trimers on a complete substrate

## Finding
Fix a trimer-attempt rate \(\lambda>0\). On \(n\) initially empty labeled sites, each unordered pair attempts irreversible two-site adsorption at independent Poisson rate \(1\), and each unordered triple attempts irreversible three-site adsorption at independent Poisson rate \(\lambda\). An attempt succeeds precisely if every site in that pair or triple is empty. Let \(U_n\) be the terminal number of empty sites. For \(n\ge2\), necessarily \(U_n\in\{0,1\}\).

Define, for \(0\le t\le1\),
\[
K(t)=\int_0^t\frac{s}{1+s+s^2}\,ds
=\frac12\log(1+t+t^2)-\frac1{\sqrt3}\left[\arctan\left(\frac{2t+1}{\sqrt3}\right)-\frac\pi6\right],
\]
and put \(\alpha=3/\lambda\), \(a=\alpha-1>-1\). Then the terminal-vacancy law converges without restricting \(n\) to residue classes:
\[
U_n\ \xrightarrow[n\to\infty]{\mathrm{law}}\ \operatorname{Bernoulli}(L_\lambda),\qquad
L_\lambda=\frac{e^{\alpha K(1)}}3\left[1+a\int_0^1 t^{a-1}\left(e^{-\alpha K(t)}-1\right)\,dt\right]. \tag{1}
\]
The integrand is integrable for every \(\lambda>0\), including \(\lambda=3\), where \(a=0\) and the integral term vanishes. In that case the limit has the elementary closed form
\[
L_3=\frac{1}{\sqrt3}\exp\left(-\frac\pi{6\sqrt3}\right)=0.4267290381001357702\ldots. \tag{2}
\]
There are two singular endpoint regimes:
\[
\lim_{\lambda\downarrow0}L_\lambda=\frac12,
\qquad \lim_{\lambda\to\infty}L_\lambda=\frac13. \tag{3}
\]
At exactly \(\lambda=0\), however, \(U_n\) is deterministically the parity of \(n\), so that its full-sequence law does not converge. Similarly, a pure-trimer limit taken before the large-substrate limit retains a three-class residue dependence. Thus any fixed positive rate of the minority species eliminates the corresponding arithmetic size oscillation in the final vacancy law.

## Assumptions and scope
The substrate is a complete two-/three-uniform hypergraph on \(n\) vertices: all pairs and all triples are allowed placements. Independent Poisson attempts have rates per **individual** pair or triple, not normalized total attempt rates. Attempts on already occupied sites are rejected. The two- and three-site objects are permanent, and there is no detachment or diffusion. The positive constant \(\lambda\) stays fixed as \(n\to\infty\). Only final vacancy counts, not adsorption times, are asserted.

## Proof
**1. Reduction to a two-step/three-step recursion.** When exactly \(k\ge3\) sites are still empty, the total successful dimer and trimer rates are \(\binom{k}{2}\) and \(\lambda\binom{k}{3}\), respectively. The next accepted event therefore removes two sites with probability
\[
q_k=\frac{3}{3+\lambda(k-2)}
\]
and three with probability \(p_k=1-q_k\). Write \(u_k=\Pr(U_k=1)\), for a process initialized with \(k\) empty sites. The complete-substrate symmetry gives
\[
u_0=0,\quad u_1=1,\quad u_2=0,\quad
u_k=q_k u_{k-2}+p_k u_{k-3}\quad(k\ge3). \tag{4}
\]
Here \(u_0\) and \(u_1\) encode already-terminal systems, and at two sites a dimer eventually deposits with probability one. At any \(k\ge2\), some dimer is feasible, proving \(U_n\in\{0,1\}\).

**2. Existence of a common large-substrate limit.** Let \(v_k=(u_k,u_{k-1},u_{k-2})^{\mathsf T}\) and
\[
M_k=\begin{pmatrix}0&q_k&1-q_k\\1&0&0\\0&1&0\end{pmatrix},
\qquad v_k=M_kv_{k-1}. \tag{5}
\]
Every \(M_k\) is row-stochastic, so the maximum and minimum of the components of \(v_k\) are respectively nonincreasing and nondecreasing. Set \(q_j=q\), \(q_{j+1}=r\), \(q_{j+2}=s\). Direct multiplication gives
\[
M_{j+2}M_{j+1}M_j=
\begin{pmatrix}1-s&qs&s(1-q)\\r&1-r&0\\0&q&1-q\end{pmatrix}. \tag{6}
\]
For sufficiently large \(j\), all three probabilities are at most \(1/2\). Any pair of rows in (6) has overlapping mass at least \(\min(q,r,s)/2\): use respectively the first, third, and second columns for row pairs \((1,2)\), \((1,3)\), and \((2,3)\). The elementary Dobrushin oscillation bound for row-stochastic matrices therefore implies that the component range contracts over each such block by at least the factor \(1-\min(q,r,s)/2\). Since \(q_k\sim3/(\lambda k)\), the sum of these blockwise minima diverges. The component range tends to zero. Its upper and lower envelopes have limits by monotonicity, hence \(u_k\to L_\lambda\) for some \(L_\lambda\in[0,1]\).

**3. Exact evaluation of the limit.** The probability generating function \(F(z)=\sum_{k\ge0}u_kz^k\), initially for \(|z|<1\), satisfies the following identity obtained by multiplying (4) by \(z^k\) and summing:
\[
\lambda z(1-z^3)F'(z)+(3-2\lambda-3z^2-\lambda z^3)F(z)=(3-\lambda)z. \tag{7}
\]
Write \(\alpha=3/\lambda\), \(a=\alpha-1\) and define
\[
I(z)=z^{a-1}(1-z^3)e^{-\alpha K(z)}\quad(0<z<1).
\]
Because \(K'(z)=z/(1+z+z^2)\), differentiating and using (7) gives
\[
\frac{d}{dz}(I(z)F(z))=a z^{a-1}e^{-\alpha K(z)}. \tag{8}
\]
Moreover \(F(z)=z+O(z^3)\) and \(K(z)=O(z^2)\) at zero. Subtracting the derivative of \(z^a\) from (8) yields the identity, valid also for negative \(a\):
\[
I(z)F(z)=z^a+a\int_0^z t^{a-1}(e^{-\alpha K(t)}-1)\,dt. \tag{9}
\]
Indeed the difference on both sides tends to zero as \(z\downarrow0\), because \(a>-1\) and \(e^{-\alpha K(t)}-1=O(t^2)\). Thus the integral is proper at the lower endpoint even for \(a<0\). By Step 2, the Abelian identity \(\lim_{z\uparrow1}(1-z)F(z)=L_\lambda\) holds. Also \(I(z)/(1-z)\to3e^{-\alpha K(1)}\), while the right side of (9) tends to the bracket in (1). This proves (1). When \(\lambda=3\), \(a=0\) so (9) gives \(F(z)=ze^{K(z)}/(1-z^3)\); inserting \(K(1)=\tfrac12\log3-\pi/(6\sqrt3)\) proves (2).

**4. The endpoint-rate limits.** As \(\lambda\to\infty\), \(\alpha\to0\), \(a\to-1\), and \(K(t)=O(t^2)\) uniformly near zero. In the bracket in (1), the integral is \(O(\alpha)\) uniformly for sufficiently small \(\alpha>0\); therefore \(L_\lambda\to1/3\). As \(\lambda\downarrow0\), \(\alpha\to\infty\), so \(a>0\) and (1) can be rewritten as
\[
L_\lambda=\frac{\alpha-1}{3}e^{\alpha K(1)}
\int_0^1 t^{\alpha-2}e^{-\alpha K(t)}\,dt. \tag{10}
\]
The phase \(\phi(t)=\log t-K(t)\) is strictly increasing, with \(\phi'(1)=2/3\), since \(\phi'(t)=(1+t)/[t(1+t+t^2)]\). A one-sided Laplace estimate gives that the integral in (10) is asymptotic to \(3e^{-\alpha K(1)}/(2\alpha)\), proving the first limit in (3). The exactly zero-rate process accepts only pairs, and the exactly pure-trimer process removes triples until fewer than three sites remain (with an available pair removing a residual pair in the present limiting-rate convention). Their distinct residue classes establish the noncommuting-limit statements.

## Verification
A standalone Python program, `verify.py`, checks the exact labeled-state Markov recursion independently against (4) for systems of up to nine sites and several rational rates, checks 595 generating-function coefficient identities using exact rational arithmetic, evaluates (1) to high precision, and compares large finite-system recursions with the quadrature at four rates. It passed 646 assertions; the full numerical output is recorded in `verification_output.txt`. These are finite and numerical consistency checks, not proofs of Steps 2–4.

To reproduce, use Python 3 and install the package named in `requirements.txt`; run `python verify.py`. Only the two local supporting files are needed.

## Relationship to prior work
Lončarević, Budinski-Petković, Vrhovac, and Belić investigated mixtures of different-length adsorbates on a **one-dimensional nearest-neighbor lattice**, analyzing coverage and kinetics numerically, including reversible variants. Their spatial finite-connectivity model neither contains the complete-substrate rate ratio in (4) nor gives (1). Penrose and Sudbury studied graph blocking and **dimer-only** deposition, deriving general occupation equations and some exact formulas on trees; these do not imply the competing complete 2-/3-hyperedge result. Pippenger's earlier random sequential adsorption on graphs treats vertex exclusion and edge dimers according to the accessible abstract; the complete-hypergraph mixed-size limit is not supplied there. These comparisons motivate the present exact mean-field jamming observable, but do not constitute exhaustive historical-priority verification.

## Limitations
The result is exact for complete mixed hypergraphs only. A complete interaction substrate is a mean-field idealization, not a statement about one-dimensional rods or physical Euclidean surfaces. It does not give the terminal counts of dimers and trimers, physical adsorption-time distributions, spatial correlations, simultaneous large-\(n\) and variable-rate scaling, or a quantitative sharp convergence rate for the vacancy probability. The existence proof via stochastic-matrix contraction gives convergence without asserting a sharp exponent. The novelty assessment is limited to the cited and inspected material, with a residual full-text access limitation for an older general graph RSA article.

## References
1. I. Lončarević, Lj. Budinski-Petković, S. B. Vrhovac, and A. Belić, "Generalized random sequential adsorption of polydisperse mixtures on a one-dimensional lattice," *Journal of Statistical Mechanics* (2010) P02022, published February 25, 2010, DOI: 10.1088/1742-5468/2010/02/P02022; accessible author manuscript at https://www.scl.rs/papers/jstat10.1088.pdf.
2. M. D. Penrose and A. Sudbury, "Exact and approximate results for deposition and annihilation processes on graphs," *Annals of Applied Probability* 15 (2005), 853–889; arXiv:math/0503519, first posted March 24, 2005, https://arxiv.org/abs/math/0503519.
3. N. Pippenger, "Random Sequential Adsorption on Graphs," *SIAM Journal on Discrete Mathematics* 2 (1989), 393–401, DOI: 10.1137/0402034; https://epubs.siam.org/doi/abs/10.1137/0402034.
