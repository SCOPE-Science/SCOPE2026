# Covariance signs and complete independence shielding in weighted even subgraphs of multipath networks

## Finding

Consider a simple graph formed by \(m\ge3\) internally vertex-disjoint paths between two terminals, with every path containing at least two edges. Independently retain edge \(e\) with probability \(p_e\in(0,1)\), and condition the resulting subgraph to have even degree at every vertex. Let \(X_i\) indicate that all edges of path \(i\) survive. Write
\[
 a_i=\prod_{e\in P_i}p_e,\quad b_i=\prod_{e\in P_i}(1-p_e),\quad
 q_i=\frac{a_i}{a_i+b_i},\quad t_i=1-2q_i,\quad T=\prod_{k=1}^{m}t_k.
\]
For every subset \(S\subseteq\{1,\dots,m\}\), every \(x\in\{0,1\}^{S}\), and the convention that an empty product equals one,
\[
\Pr(X_S=x\mid\mathrm{even})
 =\left(\prod_{i\in S}q_i^{x_i}(1-q_i)^{1-x_i}\right)
 \frac{1+(-1)^{\sum_{i\in S}x_i}\prod_{k\notin S}t_k}{1+T}.
\tag{1}
\]
In particular, for distinct paths \(i\ne j\),
\[
\boxed{\operatorname{Cov}(X_i,X_j\mid\mathrm{even})=
\frac{4q_i(1-q_i)q_j(1-q_j)}{(1+T)^2}
\prod_{k\notin\{i,j\}}t_k.}
\tag{2}
\]
Every prefactor in (2) is strictly positive. Thus the covariance's sign depends **only on the effective biases of the other paths**, not on the selected pair's own biases. Pairwise independence holds precisely when an *other* path has \(a_k=b_k\).

More generally, for every \(S\) with \(|S|\ge2\), the random variables \((X_i)_{i\in S}\) are **mutually independent** if and only if an unobserved path \(k\notin S\) has \(a_k=b_k\). This characterizes full independence, including situations in which the measured paths are strongly biased. At a homogeneous edge probability \(p\in(0,1)\), pair covariances are positive for \(p<1/2\), vanish for \(p=1/2\), and for \(p>1/2\) have sign \((-1)^{m-2}\). Consequently, networks with odd \(m\) have a sharp positive-to-negative covariance reversal at \(p=1/2\); even \(m\) have positive covariance on both sides.

## Assumptions and scope

The graph contains exactly \(m\ge3\) edge-disjoint terminal-to-terminal paths \(P_1,\dots,P_m\), with distinct internal vertices, at least two edges per path, and no other edges. This guarantees a simple finite connected graph. The independent preconditioning edge probabilities satisfy \(0<p_e<1\); they need not be equal or constant within a path. All expectations and covariances in the statements above refer to the edge law **conditioned** on every degree being even. As all \(a_i,b_i\) are positive, \(0<q_i<1\) and \(1+T>0\), so every expression is well defined. A path indicator refers to selecting its *entire* edge set; partial-path configurations have conditional probability zero.

## Proof

**Path reduction.** Every internal vertex has degree two in the underlying graph. Evenness forces its two incident edge indicators to agree. Propagating along each path shows that the retained edges are exactly a union of full paths. The two terminal degrees are both \(\sum_i X_i\), so their evenness is equivalent to \(\sum_iX_i\equiv0\pmod2\). Before imposing terminal evenness, full-path choices have weights \(a_i\) and \(b_i\). Dividing by \(a_i+b_i\) makes these choices independent Bernoulli variables with respective success probabilities \(q_i\). The overall edge-conditioning factor is
\[
\Pr(\mathrm{even})=\left(\prod_{i=1}^{m}(a_i+b_i)\right)\frac{1+T}{2}.
\tag{3}
\]
Indeed the even-parity indicator of a binary vector \(y\) equals \([1+(-1)^{\sum_i y_i}]/2\), and the mean of \((-1)^{Y_i}\) under Bernoulli\((q_i)\) is \(t_i\). All factors in (3) are positive.

**All marginals.** Fix a subset \(S\) and a status vector \(x\). Averaging the parity indicator over the independent outside bits gives \([1+(-1)^{\sum_{i\in S}x_i}\prod_{k\notin S}t_k]/2\). Divide its product-Bernoulli weight by the global even-parity probability \((1+T)/2\) to obtain (1). The formula remains valid for \(S=\varnothing\) and for \(S\) containing every path.

**Covariance.** Set \(R=\prod_{k\notin\{i,j\}}t_k\); then \(T=t_it_jR\). Formula (1) gives
\[
 \mathbb E[X_i]=\frac{q_i(1-t_jR)}{1+T},\quad
 \mathbb E[X_j]=\frac{q_j(1-t_iR)}{1+T},\quad
 \mathbb E[X_iX_j]=\frac{q_iq_j(1+R)}{1+T}.
\]
Subtraction and \(1+t_i=2(1-q_i)\) produce (2) exactly. As the prefactor is strictly positive, zero covariance is equivalent to \(R=0\), or to balancing some path other than \(i,j\). For Bernoulli variables, zero covariance is equivalent to independence of that pair.

**Complete mutual-independence criterion.** For \(|S|\ge2\), if \(R_S=\prod_{k\notin S}t_k=0\), formula (1) is the product law with marginals \(q_i\). Conversely suppose \(R_S\ne0\). Fix \(i\in S\) and any configuration \(x\) on the other elements of \(S\). Equation (1) makes the conditional odds of \(X_i=1\) against \(X_i=0\)
\[
\frac{q_i}{1-q_i}\cdot
\frac{1-(-1)^{\sum_{j\in S\setminus\{i\}}x_j}R_S}
 {1+(-1)^{\sum_{j\in S\setminus\{i\}}x_j}R_S}.
\tag{4}
\]
When \(|R_S|<1\), every configuration of the other variables has positive conditional mass, and the two parity classes give different odds because \(R_S\ne0\). Hence mutual independence is impossible. When \(|R_S|=1\), which can arise only if \(S\) exhausts the paths (all remaining \(|t_k|<1\)), both parities occur among configurations of \(S\setminus\{i\}\), but exactly one status of \(X_i\) is allowed for each such configuration. This is again incompatible with mutual independence, since \(\Pr(X_i=1)\in(0,1)\). Thus the criterion is necessary and sufficient.

**Homogeneous transition.** If each edge has probability \(p\), the effective path odds are \(a_i/b_i=[p/(1-p)]^{|P_i|}\). Therefore every \(t_i\) is positive for \(p<1/2\), negative for \(p>1/2\), and zero exactly at \(p=1/2\). Formula (2), with \(m-2\) residual factors, establishes the claimed signs without restrictions on the path lengths.

For example, in a three-path network with two edges on each path, take respective edge-probability pairs \((1/4,1/3)\), \((3/5,3/4)\), and \((1/3,2/3)\). They yield \((q_1,q_2,q_3)=(1/7,9/11,1/2)\). Although neither observed path is fair and neither edge on the third path is fair, \(X_1\) and \(X_2\) are independent after conditioning on even degrees.

## Verification

The included standalone Python 3 script `verify_theta.py` computes the exact law by exhaustively enumerating **edge-level** Bernoulli configurations and rejecting odd-degree states, independently of the path-parity proof. It compares this law to formula (1) for every status on every path subset and independently computes all pair covariances to check (2). Nine rational-parameter network examples (including homogeneous cases, heterogeneous cases, and one balanced non-fair path) pass **2,102 exact equalities** when run with `python3 verify_theta.py`. No external packages, network access, or data files are required. These finite checks corroborate, but do not replace, the unrestricted proof.

## Relationship to prior work

Grimmett and Janson, *Random Even Graphs* (first public preprint September 19, 2007; journal publication 2009), define the conditioned-Bernoulli even-subgraph law and develop couplings and sampling. Their general framework contains the present model, but the inspected statements do not present the multipath subfamily marginal law, the exact pairwise covariance sign factorization, or the if-and-only-if mutual-independence shielding criterion. These formulas are derived here from the elementary parity reduction, and no novelty is claimed for the parity-conditioning identity by itself.

Klausen (2022), Section 2 and Figures 2.1–2.2, explicitly examines three- and four-path networks and derives failure of positive association for certain **whole-cycle** events and nonmonotonic **terminal connectivity**. Hansen, Klausen, and Wildemann (2025), Section 2, similarly enumerate eight even configurations for a four-path network when computing terminal connectivity. Their finite partition functions strongly overlap with special cases of the present setup; their stated targets, however, are event-level FKG failure and connectivity, not the all-path-count, heterogeneous-weight covariance and complete-subfamily independence classifications in (1)–(4). Special cases of (2) can be algebraically recovered from such enumerations. No assertion of independent historical priority is made.

## Limitations

The result concerns a finite **multipath network** with no additional branches, chords, or boundary condition changes; it does not assert similar covariance signs for general even-subgraph graphs or random currents. The pairwise factorization is exact for arbitrary interior edge weights in \((0,1)\); endpoint weights zero or one, or infinite-volume limits, are not included. The source comparison establishes no proof of historical uniqueness; the possibility that older general parity-law or Ising-expansion results imply these formulas after specialization remains a residual priority risk. Verification exhausts only the listed finite cases, while the proof covers all specified finite networks.

## References

1. G. Grimmett and S. Janson, *Random even graphs*, arXiv:0709.3039 (first submitted 2007-09-19); *Electronic Journal of Combinatorics* 16 (2009), R46, https://doi.org/10.37236/135. General even-subgraph measure, including heterogeneous edge probabilities and couplings.
2. F. R. Klausen, *On monotonicity and couplings of random currents and the loop-O(1)-model*, *ALEA* 19 (2022), 151–161, https://doi.org/10.30757/ALEA.v19-07. See Section 2, Figures 2.1–2.2.
3. U. T. Hansen, F. R. Klausen, and P. Wildemann, *Non-uniqueness of phase transitions for graphical representations of the Ising model on tree-like graphs*, *ALEA* 22 (2025), 889–904, https://doi.org/10.30757/ALEA.v22-35. See the four-path even-subgraph enumeration in Section 2.
