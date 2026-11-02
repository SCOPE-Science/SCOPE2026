# Lucas-number ground-state census for commensurate antiferromagnetic generalized Petersen tubes

## Finding

For every integer \(r\ge2\), put \(n=4r\) and \(m=n/2=2r\). The zero-field, homogeneous antiferromagnetic Ising model on the generalized Petersen graph \(GP(n,2)\) has exactly

\[
E_{\min}=-2nJ,\qquad g(n)=4L_m,
\]

where \(J>0\) and the Lucas numbers obey \(L_0=2\), \(L_1=1\) and \(L_{k+2}=L_{k+1}+L_k\). More precisely, the labelled ground-spin configurations are in an explicit bijection with two independent Ising signs and the independent vertex sets of the cycle \(C_m\).

If exactly \(q\) of the spokes at even indices are frustrated, then the number of ground-spin configurations is

\[
g_{n,q}=4\frac{m}{m-q}\binom{m-q}{q},\qquad 0\le q\le m/2.
\]

Every ground state has separately zero outer-spin and inner-spin magnetization. The residual entropy per physical spin in the increasing-circumference sequence is

\[
\lim_{r\to\infty}\frac{\log g(4r)}{8r}=\frac14\log\left(\frac{1+\sqrt5}{2}\right).
\]

## Assumptions and scope

The graph has distinct labelled vertices \(u_i,v_i\), indexed by \(i\in\mathbb Z/n\mathbb Z\), and exactly the \(3n\) undirected edges \(u_i u_{i+1}\), \(u_i v_i\) and \(v_i v_{i+2}\). On every vertex there is one classical spin \(\sigma\in\{-1,+1\}\), which we write as \(u_i\) or \(v_i\) when no ambiguity occurs. Its energy is

\[
H=J\sum_{i=0}^{n-1}\bigl(u_i u_{i+1}+u_i v_i+v_i v_{i+2}\bigr),\qquad J>0.
\]

There is no applied field, no quantum dynamics, no disorder and no interaction beyond the stated edges. Each labelled assignment is counted once, including global spin reversal. The circumference restriction \(4\mid n\) is structural: it makes it possible to satisfy every inner edge, thereby saturating an odd-cycle frustration lower bound.

## Proof

**1. A sharp frustration inequality.** Call an edge *frustrated* if its endpoint spins agree. Let \(F_o,F_s,F_i\) be the numbers of frustrated outer, spoke and inner edges. For each \(i\), the walk

\[
u_i\,u_{i+1}\,u_{i+2}\,v_{i+2}\,v_i\,u_i
\]

is a five-cycle, with at least one frustrated edge. Every outer edge and every spoke occurs in exactly two such indexed five-cycles, whereas every inner edge occurs in exactly one. Adding the \(n\) inequalities gives

\[
n\le 2F_o+2F_s+F_i=2F-F_i\le 2F,
\]

where \(F=F_o+F_s+F_i\). Because the graph has \(3n\) edges, \(H/J=2F-3n\ge-2n\). Equality demands \(F=n/2\) and \(F_i=0\), so that

\[
v_{i+2}=-v_i.
\]

Since \(n=4r\), this condition is consistent round both inner cycles, and every such inner-spin assignment has the unique form

\[
v_{2j}=a(-1)^j,\qquad v_{2j+1}=b(-1)^j,\qquad a,b\in\{-1,+1\},
\]

where \(j\) ranges cyclically through \(0,\ldots,m-1\).

**2. Exact minimization of the outer ring.** For an arbitrary configuration with all inner edges satisfied, define \(t_j=a(-1)^j u_{2j}\) and \(s=ab\). For fixed \(a,b,t_0,\ldots,t_{m-1}\), the odd-spin contributions have coefficients

\[
(-1)^j\bigl(a(t_j-t_{j+1})+b\bigr).
\]

These are always odd, nonzero integers, and hence each odd spin has a unique minimizing value:

\[
u_{2j+1}=-(-1)^j\operatorname{sgn}\bigl(a(t_j-t_{j+1})+b\bigr).
\]

The exact elementary identity

\[
\left|a(t_j-t_{j+1})+b\right|
=1+2\mathbf1_{\{t_j=s,\,t_{j+1}=-s\}}
\]

holds for all eight combinations of \(s,t_j,t_{j+1}\), irrespective of the sign of \(a\). Let \(P=\#\{j:t_j=+1\}\), and let \(K_s=\#\{j:t_j=s,t_{j+1}=-s\}\). The resulting minimized outer-plus-spoke energy in units of \(J\) is

\[
\sum_j t_j-\sum_j\bigl|a(t_j-t_{j+1})+b\bigr|
=-2m+2(P-K_s).
\]

On a cyclic binary word, \(K_s\) counts the number of runs of \(+1\), independent of the choice \(s=\pm1\), except when there are no \(+1\) entries, in which case it vanishes. Therefore \(P-K_s\ge0\), and equality holds *exactly* when no two cyclically adjacent entries of \(t\) equal \(+1\). Equivalently,

\[
S=\{j:t_j=+1\}\in\operatorname{Ind}(C_m).
\]

Adding the \(-nJ\) from all satisfied inner edges gives \(H_{\min}=-2nJ\). The explicit unique completion above associates one ground state to every triple \((a,b,S)\), with \(a,b\in\{\pm1\}\) and \(S\) an independent set, and every ground state occurs in this way, by step 1. This proves the claimed bijection without assuming translation invariance or spin symmetry.

**3. Multiplicities.** The number of independent \(q\)-subsets of a labelled cycle with \(m\) vertices is

\[
I_{m,q}=\frac{m}{m-q}\binom{m-q}{q},\qquad 0\le q\le\lfloor m/2\rfloor.
\]

For \(q\ge1\), this follows by writing the positive cyclic gaps between chosen vertices, each at least two, and dividing the count of rooted gap descriptions by \(q\); the formula also gives \(I_{m,0}=1\). Each \(+1\) entry has \(u_{2j}v_{2j}=t_j=+1\), so \(q\) is precisely the number of frustrated even-indexed spokes. The two independent signs multiply these counts by four. Summing over \(q\) gives the standard independent-set count of a cycle, \(I(C_m)=F_{m-1}+F_{m+1}=L_m\), proving \(g(n)=4L_m\).

**4. Vanishing magnetization.** Because \(m\) is even, \(\sum_jv_{2j}=\sum_jv_{2j+1}=0\). For \(s=-1\), the explicit odd-spin minimizer and the forbidden consecutive \(+1\) entries give \(u_{2j+1}=-u_{2j}\) for every \(j\); hence the outer sum vanishes. For \(s=+1\), put \(p_j=(1+t_j)/2\). The same formula reduces to

\[
u_{2j}=a(-1)^j(2p_j-1),\qquad
u_{2j+1}=a(-1)^j(2p_{j+1}-1).
\]

The constant terms sum to zero, while \(\sum_j(-1)^j p_{j+1}=-\sum_j(-1)^j p_j\) because \(m\) is even. Therefore each outer sum also vanishes.

**5. Thermodynamic limit.** The Lucas closed form is \(L_m=\varphi^m+(-\varphi^{-1})^m\), with \(\varphi=(1+\sqrt5)/2\). As there are \(2n=4m\) physical spins, \(\log(4L_m)/(2n)\to(\log\varphi)/4\). The entropy counts exact ground states rather than finite-temperature thermodynamic states.

## Verification

The standalone `artifacts/verify_gp.py` uses only integer arithmetic and the Python standard library. It checks the proposed energy and complete ground-state count via a cyclic width-two dynamic program for all fifteen dimensions \(n=8,12,\ldots,64\); checks the constructive independent-set bijection, injectivity, refined counts and magnetization for seven sizes through \(n=32\); and exhaustively enumerates all \(2^{16}=65536\) labelled spin configurations for \(n=8\). The script prints `ALL CHECKS PASSED` and its captured output appears in `artifacts/verification_output.txt`. The proof above, not these finite tests, establishes the universal quantifiers.

For small circumferences, \(g(8)=28\), \(g(12)=72\), \(g(16)=188\), \(g(20)=492\). A separate direct check confirms the eight required absolute-value sign identities.

## Relationship to prior work

Mostovoy, Prokof'ev, Khomskii and Knoester [1] develop a frustrated Ising model on a *triangular lattice* with kink or hard-object variables, motivating exact defect descriptions but not the present generalized-Petersen formula. Besharati, Ebrahimi and Azadi [2] study independence *numbers* of generalized Petersen graphs; the independent sets in the present theorem are instead those of a *derived cycle* and count complete maximum-cut spin configurations. Varma [3] computes zero-temperature saturation-field degeneracies on different Ising ladders, a distinct model and field regime. Ewell [4] investigates maximum bipartite-subgraph *edge counts* on generalized Petersen graphs. Its accessible abstract does not establish a counting formula for all maximum cuts; the full thesis was not available for decisive comparison. The sharp energy bound may overlap such maximum-cut results, but the explicit full microcanonical classification, refined sector census and magnetization conclusion are not implied by any inspected results.

## Limitations

Only zero-temperature classical Ising states with homogeneous \(J>0\), zero field, the stated \(GP(4r,2)\) graph and \(r\ge2\) are classified. The formula does not extend automatically to other circumference residues, other generalized Petersen parameters, finite field, finite temperature, bond disorder or quantum dynamics. The work is checked analytically and by reproducible finite calculations, but priority against inaccessible specialized literature is not independently established. The known Lucas count of independent subsets of a cycle is a tool, not claimed as a new combinatorial identity.

## References

1. M. Mostovoy, N. V. Prokof'ev, D. I. Khomskii and J. Knoester, “Frustrated spin model as a hard-sphere liquid” (public preprint 2002-10-31), https://arxiv.org/abs/cond-mat/0210711 .
2. N. Besharati, J. Ebrahimi and A. Azadi, “Independence number of generalized Petersen graphs” (public preprint 2010-08-16), https://arxiv.org/abs/1008.2583 .
3. V. K. Varma, 2013 preprint on antiferromagnetic Ising ladder saturation entropy, https://arxiv.org/abs/1305.4606 .
4. L. J. Ewell, “Bipartite Density of Generalized Petersen Graphs” (2011 M.S. thesis), https://egrove.olemiss.edu/etd/1324/ .
