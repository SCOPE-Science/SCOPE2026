# A sharp stationary-error crossover for randomized edge-order exponential splitting on a directed triangle

## Finding

For the unit-rate continuous-time three-state directed cycle, consider a Lie–Trotter exponential integrator that applies each of the three single-edge Markov generators once per macro step of length \(h>0\). Compare either a fixed edge order, repeated indefinitely, or an independent uniformly random permutation of all three edges at every macro step. Both methods perform exactly three elementary exponential actions per step. The exact continuous-time equilibrium is \(u=(1,1,1)^{\mathsf T}/3\).

Let \(q=e^{-h}\in(0,1)\), and set
\[
D(q)=q^5-3q^4+4q^3-q^2+6q+2.
\]
For every initial probability vector, the randomized scheme has a unique invariant law on the probability simplex, has mean \(u\) at stationarity, and has stationary expected squared Euclidean error
\[
V(q)=\lim_{k\to\infty}\mathbb E\|X_k-u\|_2^2
=\frac{(1-q)^3(q^2-3q+4)}{3D(q)}.
\]
Among the six deterministic fixed orders, three have smaller stationary squared bias
\[
B_{\min}(q)=\frac{2(1-q)^2}{3(q+2)^2},
\]
and three have larger stationary squared bias
\[
B_{\max}(q)=\frac{2(1-q)^2}{3(1+2q)^2}.
\]
The sharp comparison between randomizing afresh and the best fixed order is
\[
V(q)-B_{\min}(q)
=-\frac{(1-q)^2\bigl[q^3(1-q)^2+2q^2+8q-4\bigr]}
{(q+2)^2 D(q)}.
\]
The polynomial \(F(q)=q^3(1-q)^2+2q^2+8q-4\) has a unique root \(q_*\in(0,1)\), numerically \(q_*\approx0.446703077326571\); put \(h_*=-\log q_*\approx0.805861161624801\). Then randomized ordering is strictly **better than all fixed orders** when \(0<h<h_*\), ties the best fixed order at \(h=h_*\), and is strictly **worse than the best fixed order but better than the worst fixed order** when \(h>h_*\). All comparisons concern the limiting expected squared Euclidean distance of the *probability vector* from the exact stationary vector; this is not pathwise error for sampled chain states.

The small-step and large-step limits are sharp:
\[
V(e^{-h})\sim\frac{2h^3}{27},\qquad
B_{\min}(e^{-h})\sim\frac{2h^2}{27}
\quad(h\downarrow0),
\]
\[
\lim_{h\to\infty}V(e^{-h})=\frac23,
\qquad\lim_{h\to\infty}B_{\min}(e^{-h})=\frac16.
\]
Thus random ordering removes the leading stationary squared-bias order for small steps, but its persistent permutation fluctuations eventually outweigh the bias of the best deterministic order.

## Assumptions and scope

Use column probability vectors \(x\in\Delta_2=\{x\in\mathbb R^3:x_j\ge0,\ \sum_jx_j=1\}\). Let \(e_1,e_2,e_3\) be the standard basis, with \(e_4=e_1\), and define the unit-rate single-edge generators
\[
Q_j=(e_{j+1}-e_j)e_j^{\mathsf T},\qquad j=1,2,3.
\]
The exact generator \(Q=Q_1+Q_2+Q_3\) has unique normalized equilibrium \(u\). For \(h>0\), the exact edge subflow is
\[
E_j(h)=e^{hQ_j}=I+(1-q)Q_j,\qquad q=e^{-h}.
\]
For each permutation \(\pi=(\pi_1,\pi_2,\pi_3)\), one macro step applies the edges in that order, so
\[
P_\pi=E_{\pi_3}E_{\pi_2}E_{\pi_1}.
\]
In the randomized method, independent uniform permutations are drawn for successive macro steps, with \(X_{k+1}=P_{\pi_k}X_k\). In a fixed-order method, the same \(\pi\) is used at all steps. Initial vectors are arbitrary deterministic points of \(\Delta_2\). Norms and expectations concern these evolving three-component *distribution vectors*, not independent CTMC sample paths.

## Proof

**Existence and symmetry.** For \(0<q<1\), every matrix \(P_\pi\) is column-stochastic. In every column \(i\), it assigns positive probability to both \(i\) and \(i+1\pmod3\): the path that stays put, and the path that makes exactly the corresponding edge transition, respectively. Thus every pair of columns shares a positive entry. The Dobrushin contraction coefficient of each \(P_\pi\) is strictly below one; taking the maximum over six permutations gives a common contraction factor \(\theta(q)<1\) on zero-sum vectors in the \(\ell^1\) norm. Coupling different starting vectors with identical permutation sequences shows that the induced Markov process on the compact simplex has a unique invariant probability law and converges to it in distribution (in fact in Wasserstein distance). These observations also imply unique stationary vectors for fixed orders.

The permutation law is invariant under cyclic relabeling. Its unique invariant law is therefore invariant under coordinate rotation. The average step matrix \(\overline P=6^{-1}\sum_\pi P_\pi\) is a positive, column-stochastic circulant matrix; hence its unique invariant vector is \(u\). Consequently \(\mathbb E X=u\) at random-order stationarity. Writing \(Z=X-u\) and \(\Pi=I-\mathbf1\mathbf1^{\mathsf T}/3\), rotation symmetry and \(\sum_jZ_j=0\) force
\[
\mathbb E[ZZ^{\mathsf T}]=\frac{V(q)}2\Pi.
\]

**Exact stationary second moment.** Each permutation is sampled independently of the present state. In the stationary covariance identity, the mixed terms vanish because \(\mathbb E Z=0\). Taking traces gives
\[
V(q)=a(q)V(q)+b(q),
\]
where
\[
a(q)=\frac1{12}\sum_{\pi}\operatorname{tr}(P_\pi\Pi P_\pi^{\mathsf T}),\qquad
b(q)=\frac16\sum_\pi\|P_\pi u-u\|_2^2.
\]
Direct multiplication of the six three-by-three edge products yields
\[
a(q)=\frac{q^6-4q^5+7q^4-5q^3+7q^2-4q+1}{3},\qquad
b(q)=\frac{(1-q)^4(q^2-3q+4)}9.
\]
In particular,
\[
1-a(q)=\frac{(1-q)D(q)}3>0,
\]
because \(D(q)=q^3(q^2-3q+4)+q(6-q)+2>0\) for \(0<q<1\). Solving the scalar second-moment identity proves the displayed formula for \(V\). Contraction and boundedness of the simplex justify convergence of the expected squared errors from every deterministic initial probability vector.

**Fixed-order stationary vectors.** Directly solving \(P_\pi x=x\) and \(\mathbf1^{\mathsf T}x=1\) gives two cyclic families. The order \((1,2,3)\) and its two cyclic shifts yield permutations of
\[
\frac{(1,q,q)^{\mathsf T}}{1+2q}.
\]
The order \((1,3,2)\) and its two cyclic shifts yield permutations of
\[
\frac{(1,1,q)^{\mathsf T}}{2+q}.
\]
Their squared distances to \(u\) give \(B_{\max}\) and \(B_{\min}\), respectively. Since \(q+2>1+2q\) for \(0<q<1\), the latter family is always optimal among fixed orders.

**Sharp crossover and the other comparison.** Substituting the exact rational expressions and canceling common factors gives the displayed formula for \(V-B_{\min}\). The derivative of its bracket is
\[
F'(q)=q^2(1-q)(3-5q)+4q+8>0
\quad(0<q<1).
\]
Indeed, the first term is nonnegative up to \(q=3/5\) and exceeds \(-2\) thereafter. Since \(F(0)=-4\) and \(F(1)=6\), there is precisely one crossing. The comparison with the largest deterministic bias is
\[
V(q)-B_{\max}(q)
=-\frac{q(1-q)^2\bigl(2q^4-6q^3+7q^2+2q+1\bigr)}{(1+2q)^2 D(q)}<0,
\]
as the last bracket equals \(q^2(2q^2-6q+7)+2q+1>0\). The asymptotics follow by evaluating these rational expressions at \(q=1\) and \(q=0\) and using \(1-e^{-h}\sim h\).

## Verification

The standalone `verify.py` (Python 3 with SymPy) constructs all six products directly, derives the average matrix, verifies the exact \(a\), \(b\), \(D\), and \(V\) identities, solves all six deterministic stationarity equations, and checks both difference factorizations. It additionally checks exact rational inputs without interpreting a finite grid as a proof of the universal inequalities. Run `python verify.py` from the directory containing that file. The universal monotonicity, sign and uniqueness arguments appear above and do not depend on that finite test set.

## Relationship to prior work

Blanes, Iserles and Macnamara developed positivity-preserving exponential methods based on graph-Laplacian representations; those constructions motivate the edge-exponential decomposition used here. Gourgoulias, Katsoulakis and Rey-Bellet analyzed long-time splitting errors for Markov models through relative entropy rates and commutators. Childs, Ostrander and Su, and Jin and Li, analyzed randomized product formulas in unitary quantum simulation. These broader frameworks do not, in the inspected material, state the exact invariant *distribution-vector* second moment for independent edge-order permutations on this Markov triangle or its unique sharp reversal against the best fixed order. The general existence of stationary covariance equations, and the general idea of order randomization, are not claimed as new. The contribution is the complete exact error-ordering and its threshold for this natural minimal Markov splitting example.

## Limitations

The theorem is specific to three equal-rate directed edges, exact subflow evaluations, independent uniform permutations, fixed positive macro-step size, and Euclidean squared distance of probability vectors to stationary equilibrium. Random-order trajectories need not converge pointwise to the equilibrium; the scheme has a nondegenerate stationary *law of distribution vectors*. Nothing is asserted for unequal edge rates, arbitrary graphs, correlated permutation schedules, other error norms, continuous-time sample-path error, or general positivity-preserving nonlinear integrators. Related results in unindexed specialized literature may exist; no independent publication-priority audit has been performed.

## References

1. S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for population models*, arXiv:2102.08242, first publicly submitted 2021-02-16; revised as *Positivity-preserving methods for ordinary differential equations*, ESAIM M2AN 56 (2022), 1843–1870. https://arxiv.org/abs/2102.08242
2. K. Gourgoulias, M. A. Katsoulakis and L. Rey-Bellet, *Information metrics for long-time errors in splitting schemes for stochastic dynamics and parallel KMC*, arXiv:1511.08240 (2015), SIAM J. Sci. Comput. 38 (2016), A3808–A3832. https://arxiv.org/abs/1511.08240
3. A. M. Childs, A. Ostrander and Y. Su, *Faster quantum simulation by randomization*, arXiv:1805.08385 (2018), Quantum 3 (2019), 182. https://arxiv.org/abs/1805.08385
4. S. Jin and X. Li, *A partially random Trotter algorithm for quantum Hamiltonian simulations*, arXiv:2109.07987 (2021). https://arxiv.org/abs/2109.07987
