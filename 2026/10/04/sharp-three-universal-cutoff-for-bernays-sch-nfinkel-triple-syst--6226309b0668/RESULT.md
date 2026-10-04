# Sharp three-universal cutoff for Bernays–Schönfinkel triple-system spectra
## Finding
Let \(R_c(3)\) denote the least integer \(r\) such that every coloring of the edges of \(K_r\) with \(c\) colors contains a monochromatic triangle. For \(k\ge 0\), put
\[
N_3(k)=k+\bigl(R_{2^k}(3)-1\bigr)2^{\binom{k}{2}}.
\]
Consider any first-order sentence about finite simple 3-uniform hypergraphs of the form
\[
\Phi=\exists x_1\cdots\exists x_k\,\forall y_1\forall y_2\forall y_3\,\psi,
\]
where \(\psi\) is quantifier-free. If \(\Phi\) has a model with more than \(N_3(k)\) vertices, then \(\Phi\) has a model of every order \(n\ge k+3\). Hence every finite spectrum in this fixed-prefix class has largest element at most \(N_3(k)\).

The endpoint is sharp for every \(k\): there is a sentence with this prefix whose spectrum is finite and whose largest model has exactly \(N_3(k)\) vertices. In particular, \(N_3(0)=2\) and \(N_3(1)=6\), because \(R_1(3)=3\) and \(R_2(3)=6\).

## Assumptions and scope
A simple 3-uniform hypergraph is represented by one symmetric irreflexive ternary relation \(E\). Equivalently, symmetry and irreflexivity can be conjoined as universal axioms without leaving a three-universal-variable prefix. Spectra count finite model orders within this class. Equality is available. The result concerns exactly three universal variables and an arbitrary fixed number \(k\) of existential variables; it does not claim an analogous closed form for larger universal blocks or for arbitrary relational vocabularies.

## Proof
Fix a model \(H\models\Phi\) and a witnessing tuple \((x_1,\ldots,x_k)\). Let \(U\) be the set of distinct witness values, so \(|U|\le k\). For a vertex \(v\notin U\), record its one-vertex witness profile
\[
\alpha(v)=\bigl(E(v,x_i,x_j)\bigr)_{1\le i<j\le k}.
\]
There are at most
\[
A=2^{\binom{k}{2}}
\]
such profiles. If \(|H|>k+(R_{2^k}(3)-1)A\), then some profile class \(C\subseteq H-U\) has at least \(R_{2^k}(3)\) vertices.

For each unordered pair \(\{u,v\}\subseteq C\), record the pair profile
\[
\beta(u,v)=\bigl(E(u,v,x_i)\bigr)_{i=1}^k\in\{0,1\}^k.
\]
Thus the edges of the complete graph on \(C\) are colored with at most \(2^k\) colors. By the definition of \(R_{2^k}(3)\), there are distinct \(a,b,c\in C\) with
\[
\beta(a,b)=\beta(a,c)=\beta(b,c).
\]
The three vertices also have the same one-vertex profile by construction.

The induced subhypergraph on \(U\cup\{a,b,c\}\), with the same witness assignment, still satisfies \(\Phi\), because the matrix after the existential witnesses is universal. Now replace \(\{a,b,c\}\) by an arbitrary set \(Z\) of at least three new vertices. Give every \(z\in Z\) the common one-vertex profile of \(a,b,c\); give every pair of distinct vertices of \(Z\) the common pair profile of the three pairs above; and set every triple of distinct vertices in \(Z\) to have the same \(E\)-value as \(E(a,b,c)\). Keep all relations on \(U\) unchanged.

Any assignment to the three universal variables uses at most three distinct vertices of \(Z\). Map those distinct vertices injectively to \(a,b,c\) and fix every witness value. This preserves equality and every possible ternary atom: atoms containing one new vertex are controlled by the one-vertex profile, atoms containing two by the pair profile, and atoms containing three by \(E(a,b,c)\); repetitions are false by irreflexivity. Therefore the truth value of every atomic formula, and hence of \(\psi\), is preserved. The enlarged structure is again a model. Choosing \(|Z|=n-|U|\) gives a model of every order \(n\ge k+3\).

For sharpness, write
\[
q=R_{2^k}(3)-1.
\]
By minimality of the multicolor Ramsey number, there is a \(2^k\)-edge-coloring \(\chi\) of \(K_q\) with no monochromatic triangle. Construct a sentence with \(k\) existential witnesses and force those witnesses to be distinct. For three distinct nonwitness vertices \(y_1,y_2,y_3\), impose the following quantifier-free implication: if the three vertices have the same one-vertex witness profile, then the three pair profiles \(\beta(y_1,y_2),\beta(y_1,y_3),\beta(y_2,y_3)\) are not all equal. This is a finite Boolean combination of atoms \(E(y_a,x_i,x_j)\), \(E(y_a,y_b,x_i)\), and equalities, so it fits the stated prefix.

In any model, every one-vertex profile class therefore carries a \(2^k\)-coloring of its complete pair graph with no monochromatic triangle, and hence has at most \(q\) vertices. There are at most \(A\) such classes, so every model has at most \(k+qA=N_3(k)\) vertices.

Equality is attained simultaneously in every profile class. Take one class \(C_\alpha\) of size \(q\) for each \(\alpha\in\{0,1\}^{\binom{k}{2}}\). Encode \(\alpha\) by the values \(E(v,x_i,x_j)\) for \(v\in C_\alpha\). Identify the \(2^k\) Ramsey colors with the bit vectors in \(\{0,1\}^k\), and encode the color \(\chi(uv)\) of each pair inside \(C_\alpha\) by the values \(E(u,v,x_i)\). Relations involving vertices from different profile classes, and triples of outside vertices, may be chosen arbitrarily. This gives a model of order exactly \(N_3(k)\), completing the sharpness proof.

## Verification
A supplementary exact checker verifies the first nontrivial multicolor calibration. It exhausts all \(2^{15}=32768\) red-blue colorings of \(K_6\), confirms that every one contains a monochromatic triangle, and verifies the standard \(5\)-cycle coloring of \(K_5\) has none. It also checks the endpoint specializations \(N_3(0)=2\) and \(N_3(1)=6\). The checker returns `VERIFY_OK R2_triangle=6 exhaustive_32768 C5_critical endpoints_k0_1=2_6`. The general theorem is proved symbolically above and does not depend on exhaustive computation.

## Relationship to prior work
The classical Bernays–Schönfinkel–Ramsey finite-model phenomenon applies to arbitrary finite relational vocabularies. Pikhurko, Spencer, and Verbitsky formulate a general recursive eventual-model bound for Bernays–Schönfinkel sentences over each fixed vocabulary. Sankaran and Chakraborty study semantic generalizations of the Bernays–Schönfinkel–Ramsey class and emphasize finite-or-cofinite spectra over relational vocabularies. For graphs, Pikhurko and Verbitsky give an explicit Ramsey-cloning proof and a coarse quantitative spectrum cutoff.

The present statement isolates the simple ternary-relation case with exactly three universal variables and computes the optimal endpoint. Unlike the graph case, two witness-interaction levels appear: \(2^{\binom{k}{2}}\) one-vertex profiles and a \(2^k\)-color pair graph inside each profile class, so the exact obstruction is the multicolor triangle Ramsey number \(R_{2^k}(3)\). Targeted searches for this fixed-prefix formula and equivalent multicolor-Ramsey formulations did not locate a published statement of the sharp endpoint.

## Limitations
The theorem does not evaluate \(R_{2^k}(3)\) in general, so exact numerical endpoints quickly inherit difficult multicolor Ramsey numbers. It is restricted to one symmetric irreflexive ternary relation and exactly three universal variables. It also does not classify which finite subsets below the endpoint occur as spectra. The main priority risk is unindexed folklore: the proof is elementary once the correct two-level profile decomposition is isolated.

## References
1. O. Pikhurko, J. Spencer, and O. Verbitsky, *Succinct definitions in the first order theory of graphs*, Annals of Pure and Applied Logic 139 (2006), 74–109. DOI:10.1016/j.apal.2005.04.003. See Proposition 2.5 for the general-vocabulary Bernays–Schönfinkel Ramsey theorem.
2. A. Sankaran and S. Chakraborty, *On Semantic Generalizations of the Bernays-Schönfinkel-Ramsey Class with Finite or Co-finite Spectra*, arXiv:1002.4334 (first posted 2010-02-23).
3. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865; Contemporary Mathematics 558 (2011), 129–180. DOI:10.1090/conm/558/11050. See Section 7.3 for the graph-spectrum Ramsey-cloning argument.
