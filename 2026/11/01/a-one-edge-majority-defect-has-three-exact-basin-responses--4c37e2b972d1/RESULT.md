# A one-edge majority defect has three exact basin responses

## Finding

Let \(a,b\ge 2\) be integers. Starting from the complete bipartite graph \(K_{a,b}\), delete exactly one edge, joining distinguished vertices \(u\) and \(v\), to obtain \(H_{a,b}\). Run simultaneous binary *open-neighborhood majority with retention on ties*: each vertex becomes the strict majority of its neighbors, or keeps its own bit if its neighborhood is tied. All configurations are labelled; a primitive temporal two-cycle is an unordered pair of distinct configurations exchanged by an update.

Write
\[
X_j=2^{j-1},\qquad C_j=\binom{j-1}{\lfloor(j-1)/2\rfloor},\qquad
\varepsilon_j=\begin{cases}1,&j\text{ even},\\0,&j\text{ odd}.\end{cases}
\]
Let \(E\) be the number of fixed configurations, \(Q\) the number of primitive two-cycle orbits, \(B\) the number of *initial* configurations whose trajectory eventually enters a primitive two-cycle, and \(T\) the maximum number of updates before a configuration first becomes periodic. Use subscripts \(0\) and \(1\) respectively for \(K_{a,b}\) and \(H_{a,b}\).

**Exact defect theorem.** For every \(a,b\ge2\),
\[
E_0=2+4\varepsilon_a\varepsilon_b C_aC_b,\qquad
B_0=2(X_a-\varepsilon_a C_a)(X_b-\varepsilon_b C_b),
\]
\[
Q_1=1,\qquad
E_1-E_0=\begin{cases}
-2C_aC_b,&a,b\text{ both even},\\
2C_o,&\{a,b\}=\{2,o\},\quad o\ge3\text{ odd},\\
0,&\text{otherwise},
\end{cases}
\]
\[
B_1-B_0=\begin{cases}
-2C_o,&\{a,b\}=\{2,o\},\quad o\ge3\text{ odd},\\
2C_eC_o,&\{a,b\}=\{e,o\},\quad e\ge4\text{ even},\ o\ge3\text{ odd},\\
0,&\text{otherwise}.
\end{cases}
\]
The unique primitive two-cycle exchanges the state with all left vertices zero and all right vertices one with its binary complement. All other recurrent configurations are fixed. The sharp worst-case entry time is
\[
T_1=\begin{cases}
4,&\{a,b\}=\{2,o\},\quad o\ge3\text{ odd},\\
3,&\{a,b\}=\{e,o\},\quad e\ge4\text{ even},\ o\ge3\text{ odd},\\
2,&\text{otherwise}.
\end{cases}
\]
Thus a single deleted edge **halves the nonunanimous equilibrium excess** in the even-even case but leaves the oscillatory basin unchanged; for mixed parity it **increases** that basin unless the even side has size two, when it **decreases** it. The exact oscillatory-orbit count stays one.

For example, \(H_{2,5}\) has \((E_1,Q_1,B_1,T_1)=(14,1,20,4)\), whereas \(K_{2,5}\) has \((E_0,B_0)=(2,32)\). For \(H_{4,4}\), these are \((20,1,50,2)\), versus \((38,50)\). For \(H_{4,5}\), they are \((2,1,196,3)\), versus \((2,160)\).

## Assumptions and scope

Graphs are finite, simple, undirected, and loopless. The two part sizes are arbitrary integers at least two. All updates are synchronous. On a tie, **the previous bit is retained**, not set to zero or randomized. The basin \(B\) includes the two periodic configurations themselves. \(T\) is the smallest nonnegative time at which \(F^{t+2}(x)=F^t(x)\), maximized over states; fixed states have entry time zero. Counts refer to labelled binary assignments, not to graph-isomorphism orbits. The theorem does not enumerate the individual basins of all fixed points.

## Proof

**1. Exact four-coordinate reduction.** Let \(A=a-1\) and \(D=b-1\). Besides the distinguished left and right bits \(u,v\in\{0,1\}\), let \(p\in\{0,\ldots,A\}\) and \(q\in\{0,\ldots,D\}\) count ones in the two undistinguished vertex sets. Define
\[
M(s,d,z)=\begin{cases}0,&2s<d,\\z,&2s=d,\\1,&2s>d.\end{cases}
\]
The simultaneous update is exactly
\[
p'=\begin{cases}0,&2(q+v)<b,\\p,&2(q+v)=b,\\A,&2(q+v)>b,\end{cases}
\qquad
q'=\begin{cases}0,&2(p+u)<a,\\q,&2(p+u)=a,\\D,&2(p+u)>a.\end{cases}
\]
The distinguished bits update as \(u'=M(q,D,u)\) and \(v'=M(p,A,v)\). This is a formula for actual *configurations*: a block is reset uniformly on a strict majority and is unchanged bitwise on a tie. Each count pair has multiplicity \(\binom Ap\binom Dq\).

**2. Uniform finite abstraction.** To certify the reduction for arbitrary dimensions rather than extrapolate from finitely many sizes, partition each count \(p\in\{0,\ldots,j-1\}\) into the following exact classes. For odd \(j=2k+1\ge3\), the classes are \(Z=\{0\}\), \(L=\{1,\ldots,k-1\}\), \(M=\{k\}\), \(H=\{k+1,\ldots,2k-1\}\), and \(O=\{2k\}\). For even \(j=2k+2\ge4\), use \(Z=\{0\}\), \(L=\{1,\ldots,k-1\}\), \(m=\{k\}\), \(p=\{k+1\}\), \(H=\{k+2,\ldots,2k\}\), and \(O=\{2k+1\}\). Empty classes are omitted. For \(j=2\), there are only \(Z=\{0\},O=\{1\}\).

In the update, the only comparisons involving a side of size \(j\) are the signs of \(2p-(j-1)\) and \(2(p+w)-j\), for \(w\in\{0,1\}\). Their complete sign patterns, shown as \((\operatorname{sgn}(2p-j+1);\operatorname{sgn}(2p-j),\operatorname{sgn}(2p+2-j))\), are:

| Side type | Class(es) | Three signs | 
| --- | --- | --- |
| odd \(j\ge3\) | \(Z,L\) | \((-;-,-)\) |
| odd \(j\ge3\) | \(M\) | \((0;-,+)\) |
| odd \(j\ge3\) | \(H,O\) | \((+;+,+)\) |
| even \(j\ge4\) | \(Z,L\) | \((-;-,-)\) |
| even \(j\ge4\) | \(m\) | \((-;-,0)\) |
| even \(j\ge4\) | \(p\) | \((+;0,+)\) |
| even \(j\ge4\) | \(H,O\) | \((+;+,+)\) |
| \(j=2\) | \(Z\) | \((-;-,0)\) |
| \(j=2\) | \(O\) | \((+;0,+)\) |

The signs determine all updates, and counts only move to zero, to the full side size, or remain exactly unchanged. Hence the class dynamics is *exactly* a finite state system. In particular, a class-level recurrent path lifts to a recurrent path of the same period for every underlying bit assignment: nonextreme counts can only be retained bitwise while the class remains nonextreme. The three universal side signatures are represented by sizes \(2,5,6\): respectively the thin class, all odd sizes at least three, and all even sizes at least four. The omitted classes at sizes three and four have multiplicity zero, so they do not affect counts or sharp entry times (the surviving classes still realize the maxima).

For a side with \(X=X_j\) and \(C=C_j\), the binomial weights of its classes are: \(Z,O\) each have weight one; for odd \(j\ge3\), \(M\) has weight \(C\), while \(L,H\) each have weight \((X-C)/2-1\); for even \(j\ge4\), \(m,p\) each have weight \(C\), while \(L,H\) each have weight \(X/2-C-1\); and \(j=2\) has only two singleton classes. These weights sum to \(2^{j-1}\) in each case. Thus symbolic summation over at most six classes per side and the two distinguished bits gives an all-parameter identity, not a finite-size conjecture.

**3. Complete symbolic class census.** Using the preceding sign table, apply the four-coordinate update until the pair of class states repeats. Summing the product of class weights over fixed recurrent states, two-cycle states, and the entire two-cycle basin gives the following exhaustive six unordered side-type cases. The middle column counts the two individual states in the unique primitive two-cycle, not the orbits:

| Sizes | \(E_1\) | Two-cycle states | \(B_1\) | Sharp \(T_1\) |
| --- | --- | --- | --- | --- |
| \(2,2\) | \(4\) | \(2\) | \(2\) | \(2\) |
| \(2,o\), odd \(o\ge3\) | \(2+2C_o\) | \(2\) | \(2(X_o-C_o)\) | \(4\) |
| \(2,e\), even \(e\ge4\) | \(2+2C_e\) | \(2\) | \(2(X_e-C_e)\) | \(2\) |
| odd \(o,o'\ge3\) | \(2\) | \(2\) | \(2X_oX_{o'}\) | \(2\) |
| odd \(o\ge3\), even \(e\ge4\) | \(2\) | \(2\) | \(2[X_oX_e-C_e(X_o-C_o)]\) | \(3\) |
| even \(e,e'\ge4\) | \(2+2C_eC_{e'}\) | \(2\) | \(2(X_e-C_e)(X_{e'}-C_{e'})\) | \(2\) |

This is an explicit finite symbolic calculation: every state has at most \(6\cdot6\cdot4\) class/bit combinations, and each step is specified by the sign table and the four-coordinate rule. The accompanying standalone program performs and checks the polynomial identities coefficientwise (not by interpolating finitely many integer sizes). Sharpness follows because the maximum-entry class in each row is populated already by its minimal representative, and remains populated at every larger size with the same signature. The recurrent two-cycle consists precisely of the two opposite-unanimous-by-part states, visibly exchanged by the rule.

**4. Undeleted benchmark.** On \(K_{a,b}\), with \(r\) and \(s\) counting ones in its full sides, the update maps each count to zero or its side size according to the other side's strict majority, retaining the entire side on a tie. Both sides tied gives \(\binom{a}{a/2}\binom{b}{b/2}\) nonunanimous fixed configurations (only when both sides are even), besides the two consensus states. The unique two-cycle has a basin exactly when the two initial full-side majorities are strict and opposite. Hence
\[
E_0=2+4\varepsilon_a\varepsilon_bC_aC_b,\qquad
B_0=2(X_a-\varepsilon_a C_a)(X_b-\varepsilon_b C_b).
\]
Subtracting these from the six cases above yields the claimed defect-response formulas, finishing the proof.

## Verification

Run `python verify_defect.py` with Python 3 and SymPy installed. The script checks the nine ordered symbolic side-signature cases as exact expanded polynomial identities; establishes two periodic states and no longer cycles for the abstract dynamics; checks \(861{,}184\) concrete quotient-compatibility instances across side sizes two through thirty; independently enumerates \(63{,}504\) actual binary starting configurations for sizes two through seven; and verifies the complete-bipartite benchmarks on \(841\) parameter pairs. The companion `verification_output.txt` is the observed output from a successful replay. The infinite-dimensional proof is the sign-class argument above; finite tests are corroboration.

## Relationship to prior work

Goles and Olivos (1980) established eventual period at most two for finite symmetric threshold systems, but not these counts or perturbation formulas. Tamuz and Tessler (first posted July 15, 2013), §3.7, explicitly used the **balanced odd** graph \(K_{d,d}\) with one edge missing and proved a two-update stabilization property for it within a larger network construction. That pre-existing result directly covers the corresponding *upper entry-time bound*, and the majority-of-sides argument also yields its odd-balanced basin as a straightforward deduction. Neither result establishes the even-even equilibrium halving, the two-by-odd reversal, the general unequal-side exact basin responses, or the mixed-parity sharp three/four-step distinctions. Kaaser, Mallmann-Trenn and Natale (first posted August 14, 2015), especially their module contraction and convergence bounds, address worst-case voting time for arbitrary graphs rather than this exact all-parameter periodic-state and basin census. The novelty claim is for the combined **all-part-sizes perturbation census**, not for the general two-cycle theorem or the previously studied balanced odd stabilization.

## Limitations

The result assumes exactly one deleted edge and side sizes at least two. It is not a count for a deleted matching of arbitrary length, nor a complete breakdown of the fixed-point basins. No independent external audit has been conducted. Historical literature may contain equivalent formulas in a different guise; searches and full-text comparisons are evidence of noncoverage, not a proof of universal priority. The technical scope is finite synchronous unweighted tie-retaining majority, not random-tie or asynchronous dynamics.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189. DOI: `10.1016/0012-365X(80)90121-1`. The publicly accessible abstract was reviewed; complete text was not available.
2. O. Tamuz and R. J. Tessler, *Majority Dynamics and the Retention of Information*, arXiv:`1307.4035`, first posted 2013-07-15; especially §3.7, Lemma 3.10. Lawful author full text: `https://www.tamuz.caltech.edu/papers/retention.pdf`.
3. D. Kaaser, F. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:`1508.03519`, first posted 2015-08-14; full conference version DOI: `10.4230/LIPIcs.MFCS.2016.55`, `https://drops.dagstuhl.de/storage/00lipics/lipics-vol058-mfcs2016/LIPIcs.MFCS.2016.55/LIPIcs.MFCS.2016.55.pdf`.
