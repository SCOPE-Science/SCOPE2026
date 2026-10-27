# The eleven-sector saturation threshold for fastest mixing on gear graphs

## Finding
Let \(G_n\) be the **gear graph** obtained from a wheel with \(n\) rim vertices by subdividing each rim edge once. It has one hub, \(n\) original rim vertices, and \(n\) inserted rim vertices, for \(2n+1\) vertices in total. For \(n\ge 11\), among *all* symmetric nonnegative row-stochastic matrices \(P\) supported on the edges and diagonal of \(G_n\), the minimum second-largest eigenvalue modulus is
\[
\mu_n^*=\frac{1+\sqrt{1+4(n-1)^2\cos^2(\pi/n)}}{2n}.
\]
It is attained by the **unique dihedrally invariant optimizer**, with edge probabilities
\[
p_n=\frac1n\quad\text{(hub--original rim)},\qquad
q_n=\frac{n-1}{2n}\quad\text{(original rim--inserted rim)}.
\]
Every hub and original-rim self-loop vanishes; each inserted-rim self-loop equals \(1/n\). The onset \(n=11\) is sharp for this fully saturated invariant design: at \(n=10\), choosing \(p=1/10\) and \(q\) just below \(9/20\) strictly improves on \((p,q)=(1/10,9/20)\).

The optimal spectral gap has the explicit asymptotic law
\[
1-\mu_n^*=\frac1{2n}+\frac{\pi^2/2-1/8}{n^2}+O(n^{-3}).
\]
For the maximum-degree rule, the gap is \((5-\sqrt{17})/(2n)+O(n^{-3})\). Consequently the ratio of optimal to maximum-degree spectral gaps tends to \((5+\sqrt{17})/8\), approximately \(1.1404\).

## Assumptions and scope
The graph is simple, undirected, connected, and unweighted before transition probabilities are assigned. Write the hub as \(h\), original rim vertices as \(u_j\), and inserted rim vertices as \(v_j\), with indices in \(\mathbb Z/n\mathbb Z\). Its edges are \(hu_j\), \(u_jv_j\), and \(u_jv_{j-1}\). An admissible \(P\) satisfies \(P=P^\mathsf T\), \(P\mathbf1=\mathbf1\), all entries nonnegative, and off-diagonal entries zero outside those edges. Loops are allowed as holding probabilities; edge probabilities may be zero. The objective is \(\mu(P)=\lVert P-J/(2n+1)\rVert_2\), where \(J=\mathbf1\mathbf1^\mathsf T\). Its value is the SLEM, even if an admissible matrix is reducible. The theorem proves the optimal *value*, an explicit globally optimal matrix, and uniqueness only **within the invariant two-parameter family**; it does not claim that every unrestricted optimal matrix is unique or invariant.

## Proof
**1. Reduction to two edge orbits.** The dihedral group permutes the \(u_j\) and \(v_j\) simultaneously, fixes \(h\), and acts transitively on the hub edges and separately on the outer edges. For any admissible matrix, average its permutation conjugates. The result remains feasible. Convexity and orthogonal invariance of the spectral norm give \(\mu(\overline P)\le\mu(P)\). Hence a global optimum occurs among invariant matrices. Such matrices assign probability \(p\) to every hub edge and \(q\) to every outer edge. Feasibility is exactly
\[
0\le p\le\frac1n,\qquad 0\le q\le\frac{1-p}{2}.
\]
The center, original-rim, and inserted-rim diagonal probabilities are, respectively, \(1-np\), \(1-p-2q\), and \(1-2q\).

**2. Fourier eigenblocks.** On the constant spatial-frequency subspace, using the orthonormal hub, normalized original-rim sum, and normalized inserted-rim sum, the transition matrix is
\[
R_0(p,q)=\begin{pmatrix}
1-np&\sqrt n\,p&0\\
\sqrt n\,p&1-p-2q&2q\\
0&2q&1-2q
\end{pmatrix}.
\]
It has eigenvalue \(1\). For each nonzero frequency \(k=1,\ldots,n-1\), diagonal unitary conjugation gives the Hermitian two-dimensional block
\[
B_k(p,q)=\begin{pmatrix}
1-p-2q&2q\cos(\pi k/n)\\
2q\cos(\pi k/n)&1-2q
\end{pmatrix}.
\]
Its eigenvalues are
\[
\lambda_{k,\pm}=1-\frac p2-2q\ \pm\sqrt{\frac{p^2}{4}+4q^2\cos^2(\pi k/n)}.
\]
The largest eigenvalue of \(B_1\), denoted \(L(p,q)\), is a universal lower bound for \(\mu(P)\) for an invariant chain, since it lies in the subspace orthogonal to constants.

**3. Sharp universal lower bound.** Put \(c=\cos(\pi/n)\). For \(n\ge11\), \(0<c<1\). At fixed \(p\), the derivative of
\[
L(p,q)=1-\frac p2-2q+\sqrt{p^2/4+4q^2c^2}
\]
with respect to \(q\) is strictly negative for \(q>0\), since the square root is at least \(2qc\) and hence the derivative is at most \(-2+2c<0\). The boundary value \(q=0\) follows by continuity. Thus
\[
L(p,q)\ge L\bigl(p,(1-p)/2\bigr)
= g(p):=\frac p2+\sqrt{\frac{p^2}{4}+(1-p)^2c^2}.
\]
Direct differentiation, with the sign justified by both sides being positive, gives the strict negativity of \(g'(p)\) whenever
\[
(1-p)(4c^2-1)>2p.
\]
For \(n\ge11\), \(c^2>3/4\) and \(p\le1/n<1/2\), so this holds. Therefore
\[
\mu(P)\ge L(p,q)\ge g(p)\ge g(1/n)
=\frac{1+\sqrt{1+4(n-1)^2c^2}}{2n}.
\]
Both inequalities are strict unless \(p=1/n\) and \(q=(1-p)/2\). This also proves uniqueness among invariant optimizers if that lower bound is attained.

**4. Attainment and the exact eleven-sector cutoff.** Set \(a=1/n\) and \(b=(n-1)/(2n)\). The nonconstant eigenvalues of \(R_0(a,b)\) are the two roots of
\[
\lambda^2+\frac{n-1}{n}\lambda-\frac1{n^2}=0.
\]
Their largest modulus is
\[
M_n=\frac{n-1+\sqrt{(n-1)^2+4}}{2n}.
\]
For every nonzero \(k\), the Fourier eigenvalues are
\[
\lambda_{k,\pm}=\frac{1\pm\sqrt{1+4(n-1)^2\cos^2(\pi k/n)}}{2n}.
\]
Their maximum absolute value is the positive eigenvalue for \(k=1\) (also \(k=n-1\)), exactly \(g(1/n)\). It remains to show \(g(1/n)>M_n\) for all \(n\ge11\).

For \(n\ge12\), use \(1-\cos x\le x^2/2\), \(\pi^2<10\), \(\sqrt{z^2+1}\ge z\), and \(\sqrt{z^2+4}\le z+2/z\) for positive \(z\). They give
\[
g(1/n)\ge\frac{(n-1)c+1/2}{n},\qquad
M_n\le\frac{n-1+1/(n-1)}n.
\]
The desired strict comparison follows from
\[
\frac{5(n-1)}{n^2}\le\frac12-\frac1{n-1}\quad(n\ge12),
\]
which after clearing positive denominators becomes \(n^3-13n^2+20n-10\ge0\). At \(n=12\) this is \(86>0\), and the polynomial is strictly increasing for \(n\ge12\).

For \(n=11\), \(c>1-5/121=116/121\). The exact rational inequalities
\[
\left(\frac{19199}{1000}\right)^2
<1+400\left(\frac{116}{121}\right)^2,
\qquad
104<\left(\frac{10199}{1000}\right)^2
\]
imply
\[
1+\sqrt{1+400c^2}>\frac{20199}{1000}>10+\sqrt{104}.
\]
This proves \(g(1/11)>M_{11}\), so the lower bound is attained for every \(n\ge11\).

To see sharpness of the onset, at \(n=10\) the saturated candidate \((p,q)=(1/10,9/20)\) instead has \(M_{10}>g(1/10)\). Indeed \(\cos^2(\pi/10)=(5+\sqrt5)/8<29/32<(119/125)^2\), and
\[
1+324(119/125)^2<(86/5)^2,
\qquad (46/5)^2<85,
\]
so \(1+\sqrt{1+324\cos^2(\pi/10)}<91/5<9+\sqrt{85}\). At this point \(-M_{10}\) is the isolated largest-magnitude nonconstant eigenvalue. Its derivative with respect to \(q\) is strictly negative: the derivative of the symmetric transition matrix is minus the weighted outer-edge Laplacian and its negative-mode eigenvector is not constant across primary and inserted rims. Decreasing \(q\) slightly therefore reduces \(M_{10}\), and the remaining strict spectral gaps persist. Thus the doubly saturated invariant design is not optimal at \(n=10\).

**5. Spectral-gap comparison.** Expanding the closed form at large \(n\) yields the stated expansion. Under the maximum-degree rule every edge probability is \(1/n\), and its top nonconstant rim-Fourier eigenvalue is
\[
1-\frac{5-\sqrt{1+16\cos^2(\pi/n)}}{2n}.
\]
For large \(n\) this dominates the other nonconstant modes (the radial modes approach values bounded above by \(1-\Omega(n^{-1})\), with a larger constant), giving a spectral gap \((5-\sqrt{17})/(2n)+O(n^{-3})\). Dividing the gap expansions gives \((5+\sqrt{17})/8\).

## Verification
The accompanying `verify.py` evaluates the exact rational cutoff certificates using integer arithmetic and independently constructs the full dense transition matrix. With NumPy it compares dense eigenvalues to all Fourier blocks for fourteen sizes, tests the complete feasible two-parameter grid and randomized nonuniform chains, checks row-stochasticity, demonstrates strict improvement at \(n=10\), and checks asymptotic constants. These tests are consistency checks; the universal optimality and cutoff follow from the proof above. Run with Python 3 and the version constraint in `requirements.txt`.

## Relationship to prior work
Boyd, Diaconis, and Xiao introduced the FMMC spectral-norm optimization and the maximum-degree/Metropolis baselines [1]. Boyd, Diaconis, Parrilo, and Xiao developed symmetry-block reduction and explicitly solved the *unsubdivided wheel* [2, Section 5.4.3]; the added subdivision layer here changes the nonconstant blocks from scalars to two-dimensional matrices and the radial block from two dimensions to three, producing the sharp \(n=11\) boundary. Jafarizadeh's clique-lift and pendant-subgraph results [3] concern a different structure and do not give this gear-network optimum. The proposed formulas do not follow merely by substituting a wheel parameter into [2].

## Limitations
Uniqueness is proved only among dihedrally invariant feasible matrices. No assertion is made about uniqueness of every unrestricted optimizer. The claim concerns uniform stationary distributions and symmetric discrete-time chains, not arbitrary reversible target distributions or mixing time under different definitions. The formula does not classify the true optimal probabilities for \(3\le n\le10\); it proves explicitly that the displayed saturated candidate is not optimal when \(n=10\). Independent mathematical audit has not been performed; specialized or less readily indexed gear-graph mixing literature may exist.

## References
[1] S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI 10.1137/S0036144503423264. Public electronic date 2004-10-29; full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf.

[2] S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM J. Optimization 20 (2009), 792–819, DOI 10.1137/070689413; arXiv:0709.0955, first posted 2007-09-06; full text: https://stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf.

[3] S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs*, IEEE Transactions on Signal and Information Processing over Networks 6 (2020), 88–104, DOI 10.1109/TSIPN.2020.2964211; accessible author-provided full text: https://www.researchgate.net/publication/387767555_Fastest_Mixing_Reversible_Markov_Chain_Clique_Lifted_Graphs_and_Subgraphs.
