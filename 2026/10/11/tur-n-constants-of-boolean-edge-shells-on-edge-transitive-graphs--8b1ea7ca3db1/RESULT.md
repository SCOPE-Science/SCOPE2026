# Turán constants of Boolean edge shells on edge-transitive graphs
## Finding
For every finite nonempty edge-transitive simple graph \(H=(V,E)\), put \(G=\mathbb F_2^V\), \(\Omega_H=\{0\}\cup\{e_u+e_v:uv\in E\}\), \(m=|E|\), and \(M=\operatorname{MAXCUT}(H)\). Then the Turán extremum \(\tau(H)=\sup\{\sum_{x\in G}f(x):f(0)=1,\ f\text{ positive definite},\ \operatorname{supp}f\subseteq\Omega_H\}\) satisfies \(\tau(H)=2M/(2M-m)=\chi_q(H)\), where \(\chi_q\) is Šámal's cubical chromatic number. A sharp extremizer is given by \(f(0)=1\) and \(f(e_u+e_v)=1/(2M-m)\) on every edge. For every odd cycle \(H=C_{2k+1}\), this normalized extremizer is unique and \(\tau(C_{2k+1})=4k/(2k-1)\).

This identifies a positive-definite extremal quantity on a natural Boolean support with an established graph cut/homomorphism parameter. In particular, every exact maximum-cut value for an edge-transitive graph gives the corresponding Turán constant immediately.

## Assumptions and scope
Let \(H=(V,E)\) be a finite nonempty simple edge-transitive graph. Work on the finite abelian group \(G=\mathbb F_2^V\). For an edge \(uv\), write \(e_u+e_v\) for its incidence vector, and set
\[
\Omega_H=\{0\}\cup\{e_u+e_v:uv\in E\}.
\]
A function \(f:G\to\mathbb C\) is positive definite in the standard finite-group sense. The normalization is \(f(0)=1\), and only functions supported in \(\Omega_H\) are admitted. Write \(m=|E|\) and let \(M\) be the maximum number of edges in a cut of \(H\).

The complete-graph specialization is only a corollary of the statement here; the structural content is the edge-transitive graph formula and its connection with cubical chromatic number. No assertion is made here for arbitrary non-edge-transitive graphs.

## Proof
Because \(G\) has exponent two, positive definiteness implies \(f(x)=\overline{f(-x)}=\overline{f(x)}\). Hence every edge coefficient is real. Write
\[
a_{uv}=f(e_u+e_v),\qquad W=\sum_{uv\in E}a_{uv}.
\]
Then the objective is \(1+W\).

Characters of \(G\) may be parametrized by sign vectors \(s=(s_v)_{v\in V}\in\{-1,1\}^V\), with the edge character equal to \(s_us_v\). Finite-group Bochner positivity therefore gives, for every sign vector,
\[
Q(s)=1+\sum_{uv\in E}a_{uv}s_us_v\ge0.
\]
Let \(C_s\) be the cut consisting of edges whose endpoints receive opposite signs, and put \(a(C)=\sum_{e\in C}a_e\). Since \(s_us_v=-1\) precisely on \(C_s\),
\[
Q(s)=1+W-2a(C_s),
\]
so every cut obeys
\[
a(C)\le\frac{1+W}2. \tag{1}
\]

Choose a maximum cut \(C_0\), so \(|C_0|=M\), and average (1) over its orbit under \(\operatorname{Aut}(H)\). Edge transitivity implies that every edge occurs in the same fraction of the orbit cuts. Comparing total incidences shows that this fraction is \(M/m\). Thus
\[
\frac Mm W\le\frac{1+W}2.
\]
A nonempty graph has \(M>m/2\): a uniformly random cut has mean size \(m/2\), while the empty cut has size zero, so some cut lies strictly above the mean. Hence
\[
W\le\frac{m}{2M-m},\qquad
1+W\le\frac{2M}{2M-m}. \tag{2}
\]

Set
\[
c=\frac1{2M-m},\qquad f(0)=1,\qquad f(e_u+e_v)=c
\]
for every edge. Its Fourier values are
\[
Q(s)=1+c\bigl(m-2|C_s|\bigr)\ge1+c(m-2M)=0,
\]
so this \(f\) is positive definite and attains equality in (2). Therefore
\[
\tau(H)=\frac{2M}{2M-m}. \tag{3}
\]

Šámal's fractional cut-cover parameter \(x(H)\) satisfies \(x(H)=m/M\) for edge-transitive graphs, and his cubical chromatic number is \(\chi_q(H)=2/(2-x(H))\). Substitution into (3) yields
\[
\tau(H)=\chi_q(H).
\]

For \(H=C_{2k+1}\), one has \(m=2k+1\) and \(M=2k\). Equality in the averaged cut bound forces equality in every maximum-cut inequality in the automorphism orbit. The maximum cuts are exactly the complements of single edges. Hence for every edge \(e\),
\[
W-a_e=\frac{1+W}2.
\]
All \(a_e\) are therefore equal; solving gives \(a_e=1/(2k-1)\). This proves both uniqueness and
\[
\tau(C_{2k+1})=\frac{4k}{2k-1}.
\]

## Verification
The accompanying exact-arithmetic checker enumerates all cuts for complete graphs through eight vertices, cycles through eleven vertices, and the Petersen graph. It checks the maximum-cut value, nonnegativity of every Fourier value for the displayed extremizer, equality of the objective with the closed formula, and the odd-cycle rigidity equations. These finite computations corroborate the implementation of the formulas; the theorem for all finite edge-transitive graphs is proved by the argument above and does not rely on enumeration.

## Relationship to prior work
Kolountzakis and Révész formulate the Turán extremal problem for positive-definite functions on locally compact abelian groups and treat finite abelian groups by Fourier methods. Their finite-group results provide the ambient harmonic framework, but the inspected finite-group theorem is expressed through spectral-set/tiling bounds rather than maximum cuts or cubical colorings.

Šámal introduces fractional covering by cuts and cubical chromatic number, proves that for edge-transitive graphs the fractional cut-cover parameter equals \(m/M\), and records exact examples such as odd cycles and the Petersen graph. The inspected paper contains no occurrence of “positive definite” or “Fourier”; it does not state the Boolean-shell Turán identity or classify the corresponding positive-definite extremizers. The statement above supplies the missing Fourier/cut bridge. Later fractional cut-cover work develops graph-theoretic and optimization aspects of the same cut parameter, without changing this comparison.

## Limitations
The proof uses edge transitivity at the automorphism-averaging step. The corresponding formula is not claimed for general graphs. The odd-cycle equality classification is complete, but no complete equality classification is asserted for every edge-transitive graph. A residual originality risk is that an equivalent bridge may exist in older literature under positive-type kernels on Cayley graphs, cut-polytopes, or cubical embeddings; targeted searches under those aliases did not locate such a statement.

## References
1. M. N. Kolountzakis and Sz. Gy. Révész, “Turán's extremal problem for positive definite functions on groups,” arXiv:math/0312218, first posted 2003-12-10.
2. R. Šámal, “Cubical coloring — fractional covering by cuts and semidefinite programming,” arXiv:0911.2589, first posted 2009-11-13.
3. J. M. M. Proença, V. A. Rodrigues, F. M. de Oliveira Filho, and C. Vinzant, work on weighted fractional cut covers and maximum-cut gauge duality, arXiv:2311.15346.
