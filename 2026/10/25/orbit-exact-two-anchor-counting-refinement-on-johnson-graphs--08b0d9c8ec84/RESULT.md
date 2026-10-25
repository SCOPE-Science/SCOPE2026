# Orbit-exact two-anchor counting refinement on Johnson graphs

## Finding
For every \(n\ge2k\ge6\), consider the Johnson graph \(J(n,k)\) with **two distinct vertices individually colored** and all other vertices initially sharing one color. Ordinary one-dimensional counting color refinement reaches precisely the orbits of the automorphisms fixing both marked vertices by round \(k+1\). The theorem includes the exceptional complementation symmetry when \(n=2k\) and gives exact class-number and class-size formulas below. In particular, every pointwise-stabilizer orbit is definable by a unary formula of two-variable first-order logic with counting, using the two marker predicates.

## Assumptions and scope
Let \(n,k\) be integers with \(n\ge2k\ge6\). A vertex is a \(k\)-element subset of \([n]=\{1,\ldots,n\}\). Two vertices are adjacent exactly when one is obtained from the other by deleting one element and inserting one different element. Fix distinct vertices \(A,B\); give them different individual colors and every other vertex a third color at round zero. At each subsequent round the color of a vertex is its previous color together with the multiset of previous colors of its neighbors. Refinement is simultaneous and never merges old color classes.

Write \(r=|A\setminus B|=|B\setminus A|\ge1\) and partition the ground set into disjoint blocks \(C=A\cap B\), \(P=A\setminus B\), \(Q=B\setminus A\), \(D=[n]\setminus(A\cup B)\), with respective sizes \(c=k-r,r,r,e=n-k-r\). For a vertex \(S\), let its profile be
\[
(a,b,h,d)=\bigl(|S\cap C|,|S\cap P|,|S\cap Q|,|S\cap D|\bigr).
\]
Feasible profiles have nonnegative integral coordinates satisfying \(a+b+h+d=k\), \(a\le c\), \(b,h\le r\), and \(d\le e\).

For \(n>2k\), each feasible profile is exactly one final color class, containing
\[
\binom ca\binom rb\binom rh\binom ed
\]
vertices. The number of classes is
\[
[z^k](1+z+\cdots+z^c)(1+z+\cdots+z^r)^2(1+z+\cdots+z^e).
\]
For \(n=2k\), put \(e=c\). Final classes are the one- or two-profile sets of the involution
\[
\iota(a,b,h,d)=(c-d,r-h,r-b,c-a).
\]
The number of classes is
\[
\frac12\left([z^k](1+z+\cdots+z^c)^2(1+z+\cdots+z^r)^2+(c+1)(r+1)\right).
\]
Their sizes are the sum of the above multinomial products over the distinct profiles in the class. These counts refer to colors of a **fixed two-marked graph**, not to graph isomorphism types.

## Proof
**1. Distance data are recovered.** The distance in \(J(n,k)\) is \(\operatorname{dist}(S,T)=k-|S\cap T|\), because each exchange can increase an intersection by at most one, and the required exchanges attain equality. Since each of \(A,B\) has a unique initial color, induction on round \(j\) shows that a vertex's color at round \(j\) determines its truncated distances \(\min(\operatorname{dist}(S,A),j+1)\) and \(\min(\operatorname{dist}(S,B),j+1)\). Indeed the distance-\(j\) frontier of each singleton is detected by adjacency to its distance-\((j-1)\) frontier, and old distinctions persist. The graph diameter is \(k\) under \(n\ge2k\). Hence at round \(k\), the color determines both
\[
x=|S\cap A|=a+b,\qquad y=|S\cap B|=a+h.
\]
(The conservative round \(k\) is used to avoid optimizing this estimate.)

**2. One more counting step recovers the profile, except for a forced symmetry.** From the colored neighbor multiset at round \(k+1\), we can recover the numbers \(f\) and \(g\) of neighbors \(T\) with respectively
\[
\bigl(|T\cap A|,|T\cap B|\bigr)=(x+1,y+1),\quad (x-1,y-1).
\]
For both intersections to increase, an exchange must delete a point in \(D\) and add one in \(C\); to decrease both, it must delete a point in \(C\) and add one in \(D\). Thus, exactly,
\[
f=d(c-a),\qquad g=a(e-d).
\]
Because \(d=k-x-y+a\), subtraction gives
\[
f-g=c(k-x-y)+(2k-n)a.\tag{1}
\]
If \(n>2k\), the coefficient \(2k-n\) is nonzero and (1) determines \(a\). Then \(b=x-a\), \(h=y-a\), and \(d=k-x-y+a\) are all determined. Hence different profiles have different colors by round \(k+1\).

If \(n=2k\), the difference in (1) has no \(a\)-term. However \(f=(k-x-y+a)(c-a)\) is a quadratic polynomial in \(a\), whose two (possibly coincident) solutions for a given \(x,y,f\) are \(a\) and \(c-(k-x-y)-a=c-d\). Substituting back into \(b=x-a\), \(h=y-a\), \(d=k-x-y+a\), the two possible profiles are precisely \((a,b,h,d)\) and \(\iota(a,b,h,d)\). Thus the color by round \(k+1\) determines the \(\iota\)-orbit of the profile.

**3. These distinctions are exactly the automorphism orbits.** Every permutation of \([n]\) preserving each of the four blocks \(C,P,Q,D\) fixes both \(A,B\) and induces a graph automorphism. Its action is transitive on the \(k\)-sets of any given profile. Therefore no color-refinement round can distinguish vertices sharing a profile. When \(n=2k\), choose any ground-set permutation \(\sigma\) interchanging \(C\) with \(D\) and \(P\) with \(Q\) (their respective sizes agree). The map \(S\mapsto[n]\setminus\sigma(S)\) is a graph automorphism, fixes both \(A,B\), and maps the profile \((a,b,h,d)\) to \(\iota(a,b,h,d)\). Consequently refinement cannot distinguish paired profiles. Steps 1–2 proved every *other* distinction by round \(k+1\), so the indicated classes are exactly the pointwise-stabilizer orbits. No assumption about the completeness of the exhibited automorphism subgroup is required: every automorphism fixing the markers preserves all refinement colors.

**4. Counting.** Counting feasible profiles is coefficient extraction from independent bounded compositions in the four blocks. In the balanced case, \(\iota\) has exactly \((c+1)(r+1)\) fixed profiles, determined by \(a+d=c\) and \(b+h=r\). Burnside's lemma for the two-element group yields the stated half-sum. The class-size formula follows by choosing the specified number of elements independently in each block. This also proves the claimed orbit definitions by the standard equivalence of finite color refinement with unary two-variable counting formulas relative to initial unary colors.

## Verification
The standalone script `johnson_refinement_verify.py` constructs labeled Johnson graphs, performs exact neighbor-multiset refinement, computes profile classes independently, tests both formulas in step 2 for **each** vertex, and checks the coefficient class count. It passed 91 parameter triples with \(2\le n\le12\), \(1\le k\le\lfloor n/2\rfloor\), \(1\le r\le k\), encompassing 20,739 total vertex instances. Although some tests deliberately include \(k<3\) as sanity checks, the stated theorem requires \(k\ge3\).

An independent implementation, `johnson_group_verify.py`, enumerates the concrete coordinate permutations fixing both markers, adds allowed complementation automorphisms when \(n=2k\), computes their actual vertex orbits by union-find, and separately runs color refinement from graph adjacency. It passed 30 cases through \(n=8\) comprising 808 vertex instances. Exact console outputs are included in `johnson_refinement_verify.log` and `johnson_group_verify.log`. Both programs require only Python 3. To replay, run `python3 johnson_refinement_verify.py` and `python3 johnson_group_verify.py` from the extracted package directory.

## Relationship to prior work
The construction builds on the classical Johnson association-scheme symmetry and on color refinement's connection with two-variable counting logic. Jones (2005), Ramras–Donovan (2011), and Ganesan (arXiv:1412.5055) determine the Johnson-graph automorphism groups, including the extra complementation automorphism at the balanced size; those symmetry theorems alone do **not** imply that color refinement identifies their pointwise-stabilizer orbits.

Arvind–Köbler–Rattan–Verbitsky (arXiv:1502.01255, appendix on Johnson graphs) prove the **stronger all-individualization Tinhofer property for \(J(n,2)\)**. That case is therefore prior art, not part of the new range. Their accessible treatment does not supply the present higher-rank \(k\ge3\), **two-marker** theorem or balanced-case profile enumeration. Grohe and collaborators (arXiv:1307.5697) provide general background on equitable partitions and color refinement but do not imply this special exact classification. Gavrilyuk–Goryainov treat perfect two-colorings in rank three, a different problem from stabilizer-orbit recovery after two individualizations. The explicit higher-rank distinction follows here from the double-increase/decrease neighbor counts in (1).

## Limitations
The statement concerns **exactly two distinct individually colored vertices**; it does not prove the Tinhofer property for \(k\ge3\), for arbitrary sets of individualizations, or for arbitrary graphs. The \(k+1\) round bound is a proved upper bound, not claimed sharp for every parameter. Numerical checks are finite corroboration, not proof of the universal assertion; the universal proof is the four-step argument above. Specialized earlier coverage of two-marked higher-rank Johnson graphs cannot be ruled out by a literature search; there has been no independent mathematical or publication-priority audit.

## References
1. M. Grohe, K. Kersting, M. Mladenov, E. Selman, *Dimension Reduction via Colour Refinement*, arXiv:1307.5697 (first publicly posted 2013-07-22), https://arxiv.org/abs/1307.5697.
2. A. Ganesan, *On the Automorphism Group of a Johnson Graph*, arXiv:1412.5055 (first publicly posted 2014-12-09), https://arxiv.org/abs/1412.5055.
3. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first publicly posted 2015-02-04), https://arxiv.org/abs/1502.01255. In particular, see the appendix on \(J(n,2)\).
4. G. A. Jones, *Automorphisms and Regular Embeddings of Merged Johnson Graphs*, European Journal of Combinatorics (2005), doi:10.1016/j.ejc.2004.01.012.
5. A. L. Gavrilyuk and S. V. Goryainov, *On Perfect 2-Colorings of Johnson Graphs \(J(v,3)\)*, Journal of Combinatorial Designs (first published online 2012-07-30), doi:10.1002/jcd.21327.
