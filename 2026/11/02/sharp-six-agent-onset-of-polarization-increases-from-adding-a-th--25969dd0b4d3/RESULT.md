# Sharp six-agent onset of polarization increases from adding a three-person group

## Finding

In the homogeneous-contribution, undirected-clique projection of the Friedkin–Johnsen model on **simple, connected, three-uniform hypergraphs**, give each existing hyperedge weight one. Let each innate opinion be binary, \(s_i\in\{0,1\}\), and add one previously absent three-person hyperedge of weight one. **For every network with at most five agents, centered squared equilibrium polarization cannot increase.** This is sharp: a connected six-agent hypergraph with only three initial hyperedges exhibits a strict increase when a fourth group is added. For the explicit six-agent witness below, the increase persists for **every positive weight** of the new group.

The result concerns one *additional group interaction*, not arbitrary network rewiring. Connectivity always refers to the graph of overlapping hyperedges (the two-section or clique projection).

## Assumptions and scope

Let \(3\le n\le6\) be an integer and \(V=\{1,\dots,n\}\). A simple three-uniform hypergraph is a collection \(\mathcal H\subseteq\binom{V}{3}\), with no duplicated triples and no pairwise-only edges. Every present triple has weight one and equal contribution fractions \(1/3\) for its three members. The symmetric effective pair weight is

\[
w_{ij}=\frac13\left|\{T\in\mathcal H:\{i,j\}\subset T\}\right|,\qquad i\ne j.
\]

Let \(L_{\mathcal H}\) be the usual weighted Laplacian of this projection. The unique expressed-equilibrium opinion vector is

\[
z_{\mathcal H}=(I+L_{\mathcal H})^{-1}s,
\qquad s\in\{0,1\}^n.
\]

For \(\bar z=n^{-1}\sum_i z_i\), define \(P(\mathcal H,s)=\sum_i(z_i-\bar z)^2\). Because the projection is symmetric and its Laplacian annihilates constants, \(\bar z=n^{-1}\sum_i s_i\).

**Universal finite cutoff.** For each \(n\in\{3,4,5\}\), every connected simple \(\mathcal H\subseteq\binom{V}{3}\), every binary \(s\in\{0,1\}^n\), and every absent triple \(T\in\binom{V}{3}\setminus\mathcal H\), one has

\[
P(\mathcal H\cup\{T\},s)\le P(\mathcal H,s).
\]

**Sharp witness.** For \(V=\{1,2,3,4,5,6\}\), let

\[
\mathcal H_0=\{\{1,2,5\},\{1,3,6\},\{1,4,5\}\},
\quad T=\{1,2,4\},\quad s=(0,0,0,0,1,0)^\top.
\]

Give the added triple \(T\) arbitrary weight \(t>0\), keeping all original triple weights one; write \(\mathcal H_t\) for this weighted extension. Then

\[
\boxed{P(\mathcal H_t,s)-P(\mathcal H_0,s)
=\frac{2t(553t+424)}{8427(19t+53)^2}>0.}
\]

In particular, the unit-weight increase is \(977/21842784\). The original three triples already form a connected hypergraph on six vertices. Three is the fewest hyperedges that any connected three-uniform hypergraph on six vertices can have.

## Proof

**1. Exact projection and positivity.** A three-person hyperedge of weight \(h\) generates three undirected pair edges, each of weight \(h/3\), by the homogeneous clique-projection formula. Define the integer matrix

\[
M(\mathcal H)=3I+\sum_{T\in\mathcal H}\ \sum_{\{i,j\}\subset T}
(e_i-e_j)(e_i-e_j)^\top.
\]

Thus \(M(\mathcal H)=3(I+L_{\mathcal H})\). Since \(I+L_{\mathcal H}\) is positive definite, rational Gaussian elimination computes the equilibrium exactly as \(z=3M(\mathcal H)^{-1}s\). The denominator never vanishes. No floating-point bound is used to decide signs.

**2. Exhaustive proof of the universal cutoff.** The accompanying `verification.py` is an executable, finite exhaustive proof. For each \(n\in\{3,4,5\}\) it generates the complete lexicographic list of \(\binom n3\) available triples and every subset (all hypergraphs), retaining those with connected two-section, tested by exact graph reachability/union–find. For each retained hypergraph it enumerates *every* absent triple. For each pair it compares exact rational polarization values for all binary innate-opinion vectors, modulo simultaneous complementation.

For this last reduction, put \(u=2s-\mathbf1\in\{-1,+1\}^n\). Since the equilibrium operator is linear and fixes \(\mathbf1\), \(z(s)=(z(u)+\mathbf1)/2\), and therefore \(P(s)=P(u)/4\). Replacing \(u\) by \(-u\) leaves polarization unchanged. It suffices to fix the first entry of \(u\) at \(+1\) and enumerate the remaining \(2^{n-1}\) sign patterns.

The exact exhaustive census is:

| Number of agents | Connected labeled triple-only hypergraphs | Eligible hypergraph–new-group pairs | Exact representative-opinion comparisons | Strict increases |
|---|---:|---:|---:|---:|
| 3 | 1 | 0 | 0 | 0 |
| 4 | 11 | 16 | 128 | 0 |
| 5 | 958 | 4,610 | 73,760 | 0 |

The verification code generates these figures from the defining loops and asserts them, while checking every inequality with Python's exact `Fraction` arithmetic. The exhaustive search is finite and includes all connected labeled systems, not a statistical sample or a numerical tolerance test. This proves the universal claim for \(n\le5\).

**3. Exact six-agent witness.** In the displayed six-agent system, the equilibrium after adding \(T\) with weight \(t\ge0\) is

\[
z(t)=\frac1{3(19t+53)}
(8t+24,\ 8t+21,\ 2t+6,\ 8t+21,\ 29t+81,\ 2t+6)^\top.
\]

This identity follows by direct substitution into \((I+L_{\mathcal H_t})z=s\); the numerator and denominator are linear in \(t\). In particular, \(\sum_i z_i(t)=1\), so \(\bar z=1/6\). Squaring and summing centered entries gives

\[
P(\mathcal H_0,s)=\frac{2585}{16854},\qquad
P(\mathcal H_1,s)=\frac{1193}{7776},
\]

and the rational difference displayed above. Both \(553t+424\) and \(19t+53\) are positive for \(t>0\), giving the strict inequality for *every* positive new-group weight. The standalone checker certifies the polynomial coefficients of both the equilibrium equations and the exact rational polarization identity.

**4. Minimality of the initial number of groups.** Two distinct triples on six vertices either are disjoint (so their two-section is disconnected) or share at least one vertex (so their union contains at most five vertices). Thus a connected six-vertex three-uniform hypergraph requires at least three triples. The witness attains this lower bound.

## Verification

Run `python3 verification.py` with Python 3 and no third-party packages. It prints, among other checks, `n=4 connected=11 exact_signed_addition_checks=128`, `n=5 connected=958 exact_signed_addition_checks=73760`, `zero_one_binary_increase= 977/21842784`, `all_positive_group_weights_algebraic_identity=PASS`, and `EXACT VERIFICATION PASSED`.

The file itself includes every defining loop, the full integer-matrix construction, exact Gaussian elimination, the connectedness check and coefficient identities. The witnessed inequality is established both by exact rational inversion at unit weight and by a symbolic-in-\(t\) coefficient certificate. The binary-opinion normalization is tested explicitly.

## Relationship to prior work

Xu and Zhang, *Linear Opinion Dynamics Model with Higher-Order Interactions* (arXiv:2310.05689v1, 9 October 2023), introduce both the homogeneous undirected clique projection and asymmetric directed projection of group interactions, and analyze differences in equilibrium opinion and polarization (Sections III and V). The present work **uses their homogeneous model**, not a new influence rule. Their numerical comparisons between projections do not give the sharp minimal number of agents for a binary-opinion increase when **one homogeneous triple is added to a connected triple-only hypergraph**.

Rácz and Rigobon, *Towards Consensus: Reducing Polarization by Perturbing Social Networks* (arXiv:2206.08996v2, 20 December 2022), derive effects of changing individual pairwise weights and show that added attractive connections need not decrease polarization when innate opinions are unrestricted. Their formula provides a mechanism for nonmonotonicity under positive Laplacian perturbations, but is not by itself a classification under the constraints of unit-weight three-person group interactions, triple-only connectivity, and binary opinions. Such a group creates a three-edge clique simultaneously; it is not a single pairwise-edge addition.

The conclusions are a specific finite structural cutoff and an exact, minimally connected witness, **not** a claim that positive-edge nonmonotonicity or higher-order FJ opinion dynamics were previously unknown.

## Limitations

The cutoff is for simple, connected, three-uniform hypergraphs with all pre-existing groups of weight exactly one, equal member contributions, and **one new group of weight one**, with binary innate opinions. It is not asserted for heterogeneous group contributions, directed projection, arbitrary pre-existing weights, pairwise-only hyperedges, arbitrary real-valued opinions, or more than one new group. The formula for arbitrary positive added weight belongs only to the explicit six-person witness. For networks of seven or more agents no enumeration or classification is claimed. The correctness certificate is a transparent finite exhaustive calculation for the small-network assertion, not a symbolic classification at arbitrary network sizes. No independent audit is claimed.

## References

1. W. Xu and Z. Zhang, *Linear Opinion Dynamics Model with Higher-Order Interactions*, arXiv:2310.05689v1 (first public 9 October 2023), https://arxiv.org/html/2310.05689v1; see equations (2), (3) and Section V-C.
2. M. Z. Rácz and D. E. Rigobon, *Towards Consensus: Reducing Polarization by Perturbing Social Networks*, arXiv:2206.08996v2 (20 December 2022; first public 17 June 2022), https://arxiv.org/html/2206.08996v2; see Section 4.2 and the edge-weight sensitivity formula.
