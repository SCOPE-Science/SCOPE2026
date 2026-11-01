# A density-sharp variation defect for binary path data without triple zero runs

## Finding
For a finite path with binary data, the total-variation deficit of the centered maximal operator admits an exact sum over zero runs when all such runs have length at most two. This yields a support-dependent sharp inequality on a class with arbitrarily many separated support components, an exact equality test using centered-ball zero densities, and an explicit example showing why three-zero runs escape the local two-level argument.

For \(n\ge3\), suppose \(f:P_n\to\{0,1\}\) is nonconstant and \(000\) does not occur as a consecutive word. Write \(m=|\{j:f(j)=0\}|\). Then
\[\boxed{\operatorname{Var}(Mf)\le\frac{m}{n}\operatorname{Var}(f).}\]
More precisely, with the definitions below,
\[\boxed{\frac{m}{n}\operatorname{Var}(f)-\operatorname{Var}(Mf)=\sum_{R}b_R\left(\frac{m}{n}-H_R\right).}\]
Each term is nonnegative. Equality is characterized exactly by a finite test of all centered-ball zero fractions, and the coefficient is attained for every \(n\ge3\) by an indicator with one zero. Since \(m\le n-1\), this implies the conjectured finite-path coefficient on the stated class, including highly nonunimodal inputs.

## Assumptions and scope
Identify \(P_n\) with the vertex set \(\{1,\ldots,n\}\) and edges between successive integers. The graph ball is
\[B_r(j)=\{i:1\le i\le n,\ |i-j|\le r\},\qquad r\in\{0,1,\ldots,n-1\}.\]
For \(f:P_n\to\{0,1\}\), define
\[(Mf)(j)=\max_{0\le r<n}\frac1{|B_r(j)|}\sum_{i\in B_r(j)}f(i),\qquad
\operatorname{Var}(g)=\sum_{j=1}^{n-1}|g(j+1)-g(j)|.\]
Suppose \(f\) contains at least one zero and one one and no zero run exceeds two vertices. Let \(Z=\{j:f(j)=0\}\), \(m=|Z|\), and \(h=1-Mf\). Let \(\mathcal R\) be the maximal intervals of consecutive zero vertices. For \(R\in\mathcal R\) define \(b_R=2\) if \(R\) meets neither endpoint, and \(b_R=1\) otherwise; define \(H_R=\max_{j\in R}h(j)\). As \(f\) is nonconstant, no zero run can meet both endpoints without meeting a one vertex elsewhere; any run meeting an endpoint has exactly one boundary edge. The theorem is homogeneous for \(cf\), \(c>0\), after both variations are multiplied by \(c\).

## Proof
**Step 1 (zero-density representation).** On each ball \(B\), the average of \(f\) is \(1-|B\cap Z|/|B|\). Hence
\[h(j)=\min_{0\le r<n}\frac{|B_r(j)\cap Z|}{|B_r(j)|}.\]
At a one vertex the radius-zero ball gives \(h(j)=0\). At each zero vertex, every radius ball contains that vertex, and the largest ball is all of \(P_n\), so
\[0<h(j)\le m/n.\]

**Step 2 (endpoint zero pairs have identical heights).** Suppose \(f(1)=f(2)=0\). Every centered ball about vertex \(1\) is a prefix \(\{1,\ldots,t\}\), \(1\le t\le n\). Every centered ball about vertex \(2\) is either the singleton \(\{2\}\) or a prefix \(\{1,\ldots,t\}\) of length \(t\ge3\) (with clipping at \(n\)). The missing prefixes of lengths one and two have average \(f\) equal to zero. These observations give \((Mf)(1)=(Mf)(2)\), and therefore \(h(1)=h(2)\). The same statement holds at the right endpoint by reflection. In particular, a boundary zero run of length two contributes exactly its height, rather than a potentially larger oscillatory term, to the total variation of \(h\).

**Step 3 (runwise exact identity).** On all one vertices \(h=0\). An interior zero singleton with height \(a\) contributes \(2a\) to the two adjacent edges; an interior zero pair with heights \(a,b\) contributes
\[a+|a-b|+b=2\max(a,b).\]
A boundary singleton contributes its single height, and a boundary pair contributes the common height by Step 2. All edges that join one vertices contribute zero; different maximal zero runs are separated by at least one one vertex, so their edge contributions do not overlap. Consequently
\[\operatorname{Var}(Mf)=\operatorname{Var}(h)=\sum_{R\in\mathcal R}b_RH_R,\qquad
\operatorname{Var}(f)=\sum_{R\in\mathcal R}b_R.\]
Subtracting gives exactly the asserted nonnegative deficit identity.

**Step 4 (sharpness and complete equality test).** Equality holds precisely when \(H_R=m/n\) for each run. Because the entire path is a centered ball about every vertex, Step 1 implies that this happens precisely when some \(j\in R\) has every centered ball \(B\) about it satisfying
\[\frac{|B\cap Z|}{|B|}\ge\frac mn,\qquad\text{equivalently}\qquad n|B\cap Z|\ge m|B|.\]
This is a finite integer inequality certificate and is both necessary and sufficient. For every path length, choose any binary sequence with exactly one zero; at that vertex any ball has zero fraction at least \(1/n\), while the full ball has exactly \(1/n\). Thus equality holds and the coefficient cannot be reduced uniformly. The equality class is not confined to a single zero: \(f=(1,1,0,1,0,1,0,1,1)\) on \(P_9\) has three separated zeros and satisfies the criterion at each zero, giving \(\operatorname{Var}(Mf)=2=(3/9)\operatorname{Var}(f)\).

**Step 5 (exact structural boundary of the local mechanism).** For \(P_7\), take \(f=(0,1,0,0,0,1,0)\). The maximal function on vertices \(2,3,4,5,6\) is \((1,1/3,2/5,1/3,1)\). Therefore the variation across the three-zero run between the two adjacent ones is
\[\frac23+\frac1{15}+\frac1{15}+\frac23=\frac{22}{15}.\]
Here \(m=5\), so its nominal density budget of \(2m/n=10/7\) is strictly smaller. The runwise identity proved above therefore cannot be extended verbatim to length-three zero runs; this is not a counterexample to any global path-variation conjecture.

## Verification
The accompanying standalone Python checker performs exact rational evaluation of all graph-ball maxima for every nonconstant binary sequence avoiding \(000\) on every path of length three through fourteen. It verifies both the defect identity and the ballwise equality criterion, including endpoint zero pairs and three-separated-zero extremizers. It separately checks the length-three local boundary example. Computation is a consistency check and is not used as an infinite proof; Steps 1–5 are valid for all finite lengths.

## Relationship to prior work
González-Riquelme, Kovač and Madrid [1] defined the graph variation problem and conjectured the unrestricted coefficient \(1-1/n\) for every finite path. The result here proves the strictly stronger support-dependent coefficient \(m/n\) on an explicit nonunimodal class, while leaving the conjecture for general data and longer zero gaps open.

Bilz and Weigt [2] proved the global contraction of centered maximal variation for indicator functions on \(\mathbb Z\), a different operator and coefficient; the infinite-lattice bound alone does not imply the present density-sensitive finite-path deficit. Hagelstein, Kosz and Stempak [3] developed an endpoint variation improvement for functions with gaps on \(\mathbb R\) and \(\mathbb Z\), but do not state this finite-path support-density identity. Previous work on unimodal finite-path input gives peak-position refinements, not this many-component binary zero-run result.

## Limitations
The theorem assumes binary inputs with zero runs of length at most two; it does not settle the full finite-path conjecture, does not address arbitrary real-valued data, and does not claim that the density coefficient holds for every binary input. The three-zero example only obstructs the local two-height proof method, not the global inequality. The literature comparison is a best-knowledge assessment, not independent certification of publication priority.

## References
[1] C. González-Riquelme, V. Kovač, J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462v1, first public March 12, 2026, https://arxiv.org/abs/2603.12462.

[2] C. Bilz and J. Weigt, *The one-dimensional centred maximal function diminishes the variation of indicator functions*, arXiv:2107.12404 (2021); *J. Geom. Anal.* 35 (2025), article 256, https://arxiv.org/abs/2107.12404.

[3] P. Hagelstein, D. Kosz, K. Stempak, *Variation of the one-dimensional centered maximal operator on simple functions with gaps between pieces*, arXiv:2407.06734 (2024), https://arxiv.org/abs/2407.06734.
