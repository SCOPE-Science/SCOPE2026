# Sharp finite-field graph-support spectrum for a single square-dependence pair

## Finding
Let \(q\) be any prime power, \(n\ge3\), and let \(E\) be an \(n\)-dimensional evolution algebra over \(\mathbb F_q\), with a natural basis \(e_1,\ldots,e_n\) such that \(e_i^2\ne0\) for all \(i\),
\[
e_2^2=\lambda e_1^2\quad(\lambda\in\mathbb F_q^\times),\qquad
\{e_1^2,e_3^2,\ldots,e_n^2\}\text{ is linearly independent}.
\]
Thus \(\dim E^2=n-1\) and the sole dependence block of natural-basis squares is the pair \(e_1,e_2\). Put \(U=\langle e_1,e_2\rangle\), \(B((x,y),(z,w))=xz+\lambda yw\), and let \(\pi_U:E\to U\) be the projection along \(\langle e_3,\ldots,e_n\rangle\). Write \(u_1=e_1^2\) and \(u_i=e_i^2\) for \(3\le i\le n\); put \(v_i=\pi_U(u_i)\).

Let \(\Omega\) be the set of unordered pairs \(\{L,L^\perp\}\) of distinct, nonisotropic projective lines for \(B\) in \(U\). Its cardinality is
\[
N=|\Omega|=\begin{cases}
(q-1)/2,&q\text{ odd and }-\lambda\text{ is a square},\\
(q+1)/2,&q\text{ odd and }-\lambda\text{ is a nonsquare},\\
q/2,&q\text{ even}.
\end{cases}
\]
For \(i\in\{1,3,\ldots,n\}\), ignore \(v_i=0\) and isotropic projective lines \(\langle v_i\rangle\); each remaining line determines the unique member \(\{\langle v_i\rangle,\langle v_i\rangle^\perp\}\in\Omega\). Let \(T\) be the set of members so obtained and put \(t=|T|\).

**Complete marked support-spectrum theorem.** Consider, for every natural basis, the directed graph in which an arrow records a nonzero structure coefficient. Its unique two-dimensional dependence block is identified with \(U\), and each one-dimensional block is identified with its original index \(i\ge3\); the two vertices in \(U\) are unordered. Count distinct patterns of arrows *into* the two vertices of \(U\), with arrows from the two source vertices in \(U\) identified because they have identical support. Then the number of such patterns across **all** natural bases is exactly
\[
\boxed{\quad t+\mathbf1_{t<N}.\quad}
\]
More explicitly, the pattern indexed by \(\omega=\{L,L^\perp\}\in\Omega\) has \(0\), \(1\), or \(2\) target arrows from source block \(i\in\{1,3,\ldots,n\}\): zero if \(v_i=0\), one if \(\langle v_i\rangle\in\omega\), and two otherwise. In the one-arrow case the target is specified by the line containing \(v_i\), so this also determines the full marked adjacency pattern up to the common swap of the two targets. All arrows to singleton target blocks are fixed across bases. The same formula therefore counts distinct **block-marked whole-graph support patterns** (not necessarily distinct unmarked graph-isomorphism classes).

The sharp extremal value over all such algebras with fixed \(n,q,\lambda\) is
\[
\boxed{\quad\max_E |\text{marked support-spectrum}(E)|=\min\{n,N\}.\quad}
\]
This includes the exact characteristic-two threshold \(q=2\), where every such algebra has just one natural basis up to permutation and scaling and just one graph-support pattern. For odd \(q=3\) with \(-\lambda\) a square the same rigidity holds. The orthogonal parameterization of natural bases is known in the literature; the new assertion is the complete finite-field **graph-support pattern classification and sharp extremum**.

## Assumptions and scope
The multiplication satisfies \(e_i e_j=0\) for \(i\ne j\). All fields in the result are finite fields, including extension fields of characteristic two. The dependence hypothesis is **stronger** than mere corank one: it requires one proportional pair and independent representatives of all remaining square lines. Graphs are considered with the canonical dependence-block marking; their isomorphism classes as completely unmarked digraphs are not counted.

## Proof
**(1) All natural-basis changes are block diagonal.** Let \(f_j=\sum_i p_{ij}e_i\) be another natural basis. Orthogonality \(f_jf_k=0\) for \(j\ne k\), together with the linear independence of \(u_1,u_3,\ldots,u_n\), implies
\[
p_{1j}p_{1k}+\lambda p_{2j}p_{2k}=0,\qquad p_{ij}p_{ik}=0\ (i\ge3).
\]
For each \(i\ge3\), row \(i\) of the invertible matrix \((p_{ij})\) has precisely one nonzero entry; these entries occupy distinct columns, otherwise two rows would be proportional. Permute the columns so that the last \(n-2\) columns carry the nonzero singleton rows, and the first two columns have no singleton entries. Their \(U\)-parts form a basis of \(U\). By the displayed orthogonality equations, they form a nondegenerate orthogonal basis of \((U,B)\). Every other column has \(U\)-part orthogonal to both basis vectors, hence zero. Consequently, after column permutation, every natural basis is \((\ell,m,s_3e_3,\ldots,s_ne_n)\), with \(B(\ell,m)=0\), \(B(\ell,\ell)B(m,m)\ne0\) and all \(s_i\ne0\). Conversely each such list is a natural basis. Modulo scaling and permutation, choices are exactly \(\Omega\).

**(2) Projective count.** The involution \(L\mapsto L^\perp\) on the \(q+1\) lines of \(\mathbb P(U)\) fixes exactly the isotropic lines. In odd characteristic, \(x^2+\lambda y^2=0\) has two such lines when \(-\lambda\) is a square, and none otherwise. In even characteristic, Frobenius \(a\mapsto a^2\) is a field automorphism and the equation has exactly one projective solution. Deleting these fixed points and dividing by two gives \(N\).

**(3) Graph support.** Write each \(u_i\) as \(v_i+z_i\), where \(z_i\in\langle e_3,\ldots,e_n\rangle\). Under an orthogonal basis \(\ell,m\) of \(U\), the coefficients of \(v_i\) on \(\ell,m\) vanish together exactly when \(v_i=0\); exactly one vanishes when \(\langle v_i\rangle\) equals either \(\langle\ell\rangle\) or \(\langle m\rangle\); otherwise neither vanishes. An isotropic nonzero line can never equal either basis line. The two new source squares \(\ell^2,m^2\) are nonzero multiples of \(u_1\), so they have the same support; the singleton squares are rescaled \(u_i\). The \(z_i\) contributions give fixed singleton-target arrows. This proves the detailed adjacency description.

For each \(\omega\in T\), the nonempty set of indices with exactly one arrow into \(U\) uniquely identifies \(\omega\): different orthogonality orbits have disjoint sets of contributing indices. If \(\omega\notin T\), all nonzero projected sources have two arrows and the resulting support pattern is independent of \(\omega\). Thus there are precisely \(t+\mathbf1_{t<N}\) distinct patterns.

**(4) Sharpness.** Trivially \(t\le n-1\), since there are \(n-1\) potentially nonzero square-representative directions; hence \(t+\mathbf1_{t<N}\le\min\{n,N\}\). For equality fix any \(\lambda\ne0\) and take \(e_1^2=e_1\), \(e_2^2=\lambda e_1\). Let \(\omega_0\in\Omega\) be the orbit containing \(\langle e_1\rangle\). Choose representatives \(v_i\in U\) of distinct orbits in \(\Omega\setminus\{\omega_0\}\) for the first \(\min\{n-2,N-1\}\) indices \(i\ge3\), and put \(v_i=0\) for any remaining indices. Define \(e_i^2=e_i+v_i\). The \(n-1\) representatives \(e_1^2,e_3^2,\ldots,e_n^2\) are independent, all squares are nonzero, and \(t=\min\{n-1,N\}\), giving equality in the claimed maximum.

For an explicit nontrivial example, over \(\mathbb F_5\), take \(n=3,\lambda=2\), \(e_1^2=e_1\), \(e_2^2=2e_1\), \(e_3^2=e_3+e_1+e_2\). There are three orthogonal-line pairs and the marked two-target arrow-count profiles are \((1,2)\), \((2,1)\), and \((2,2)\). These also give three nonisomorphic **unmarked** digraphs, witnessed by their different outdegree multisets \(\{1,1,3\}\), \(\{2,2,2\}\), and \(\{2,2,3\}\), respectively.

## Verification
The standalone file `verify_profiles.py` uses exact finite-field arithmetic for prime fields of orders \(2,3,5,7,11\). For every nonzero \(\lambda\), it enumerates isotropic projective lines, orthogonal-line pairs, all invertible orthogonal two-column frames, and the predicted graph profiles for sharpness examples in dimensions \(3,4,5\). It also exhaustively enumerates all invertible natural-basis changes in dimension three over \(\mathbb F_2\) and \(\mathbb F_3\) to test the block form. Running `python3 verify_profiles.py` prints `VERIFY_OK`. These finite experiments check examples only; the proof above handles every prime power and all dimensions.

## Relationship to prior work
The October 15, 2026 survey of Kaygorodov, Martín González and Viruel asks for natural-basis moduli in Question 14 and simultaneous graph realizations in Question 30. Boudi, Cabrera Casado and Siles Molina (2020), Theorem 2.11, Corollary 2.13 and Proposition 2.16, already give the underlying square-dependence blocks and orthogonal natural-basis principle. Their structural description is used here, and the rank-two orthogonality parameterization itself is **not claimed as new**. The specific classification of all marked graph-support patterns for a one-pair dependence stratum, the exceptional/generic orbit count and the attained sharp \(\min\{n,N\}\) extremum do not occur in the inspected sections. Alshatnawi, Costoya and Viruel (2026) establish a different basis-independent graph invariant, balance, without providing this graph-support spectrum.

## Limitations
The result is not a classification of all corank-one evolution algebras: it excludes more complicated square dependencies. It counts block-marked support patterns, not arbitrary unmarked digraph-isomorphism classes; the explicit \(\mathbb F_5\) example demonstrates unmarked distinctness only in that example. Over larger fields, the natural-basis parameterization and its cardinality follow readily from prior work; the graph-spectrum formula and sharp extremum are the substantive addition. There is a residual possibility of an earlier or unindexed equivalent graph-support enumeration. Independent validation has not been performed.

## References
1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first public October 15, 2026), especially Questions 14 and 30. https://arxiv.org/pdf/2610.22248
2. N. Boudi, Y. Cabrera Casado, M. Siles Molina, *Natural families in evolution algebras*, arXiv:2006.14460 (first public June 25, 2020), Theorem 2.11, Corollary 2.13 and Proposition 2.16. https://arxiv.org/pdf/2006.14460
3. I. Alshatnawi, C. Costoya, A. Viruel, *On the Grothendieck ring of finite-dimensional non-degenerate evolution algebras*, arXiv:2607.15154v1 (first public July 16, 2026), especially Theorem 6.1 on graph balance. https://arxiv.org/pdf/2607.15154
