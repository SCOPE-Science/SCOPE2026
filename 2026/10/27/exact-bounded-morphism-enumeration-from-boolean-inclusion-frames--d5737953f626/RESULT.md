# Exact bounded-morphism enumeration from Boolean inclusion frames onto a three-world chain

## Finding
For the inclusion-ordered Boolean frame \(B_n=(2^{[n]},\subseteq)\) and the three-point reflexive chain \(C_3=(\{0,1,2\},\le)\), the exact numbers \(F_n\) of globally surjective bounded morphisms for \(n=0,1,2,3,4,5\) are
\[0,\quad0,\quad3,\quad63,\quad3604,\quad3242450.\]
An all-parameter frontier characterization and an exact downset inclusion–exclusion formula determine \(F_n\) for every \(n\ge1\). The first possible quotient appears at \(n=2\), and quotients exist for all larger \(n\). In particular, the 32-world frame \(B_5\) has exactly \(3{,}242{,}450\) such morphisms, compared with \(7{,}805{,}614\) surjective order-preserving maps onto the same target.

## Assumptions and scope
Fix \(n\ge1\). Worlds of \(B_n\) are all subsets of \([n]=\{1,\ldots,n\}\); accessibility is inclusion, including reflexive loops. Worlds of \(C_3\) are \(0<1<2\), with reflexive accessibility. A bounded morphism \(f\) satisfies the forth condition \(x\subseteq y\Rightarrow f(x)\le f(y)\) and the back condition: for every \(x\in B_n\) and \(t\ge f(x)\), some \(y\supseteq x\) satisfies \(f(y)=t\). Global surjectivity is additionally required. Neither domain nor codomain is supplied with extra predicates. Counts distinguish different maps on the fixed labelled Boolean lattice, even when related by a coordinate permutation.

For any finite induced poset \(Q\), write \(\mathcal D(Q)\) for the number of its downsets, including the empty and whole downsets. An ideal/downset of \(B_n\) is a collection \(I\subseteq 2^{[n]}\) such that \(a\in I\) and \(b\subseteq a\) imply \(b\in I\). Write \(\operatorname{Max}(I)\) for its inclusion-maximal worlds and \(\operatorname{Cov}(a)=\{a\cup\{i\}:i\notin a\}\). For \(S\subseteq\operatorname{Max}(I)\), define the upset
\[U_S=\{y\in B_n:\exists a\in S,\ \exists b\in\operatorname{Cov}(a),\ b\subseteq y\}.\]
In particular \(U_\varnothing=\varnothing\).

## Proof
**1. Map/downset normal form.** Given a monotone onto map, put \(I=f^{-1}(\{0\})\) and \(J=f^{-1}(\{0,1\})\). Then \(\varnothing\ne I\subsetneq J\subsetneq B_n\) are downsets; conversely, such a pair determines one monotone onto map by assigning \(0\) on \(I\), \(1\) on \(J\setminus I\), and \(2\) on \(B_n\setminus J\). Nonempty/downset/proper are conditions on collections of worlds, not on individual Boolean subsets.

**2. The full back condition reduces to the zero frontier.** Because \(J\ne B_n\), the top Boolean world \([n]\) has image \(2\). Thus a witness for target \(2\) is available above every world. Worlds of image \(1\) need no other nontrivial witness. A world \(x\) of image \(0\) needs a witness of image \(1\) above it. Every such \(x\in I\) is below an inclusion-maximal \(a\in I\); hence it suffices to check maximal zero worlds. If \(a\in\operatorname{Max}(I)\) has a \(1\)-valued strict superset \(y\), choose the first edge of a saturated Boolean chain from \(a\) to \(y\). Its endpoint \(b\in\operatorname{Cov}(a)\) is outside \(I\), by maximality, and lies in \(J\), by downward closure of \(J\). Conversely, an immediate cover in \(J\) of a maximal \(a\in I\) necessarily has image \(1\), giving a witness. This proves the exact frontier characterization.

**3. Inclusion–exclusion.** Fix any nonempty proper ideal \(I\). Among ideals \(J\supseteq I\), let \(E_a\) denote failure to include an immediate cover of a particular \(a\in\operatorname{Max}(I)\). For \(S\subseteq\operatorname{Max}(I)\), the simultaneous failure events \(E_a\), \(a\in S\), say precisely that \(J\) avoids \(U_S\), because \(J\) is a downset. The ideals \(J\) with \(I\subseteq J\subseteq B_n\setminus U_S\) are in bijection with downsets of the induced remainder \(B_n\setminus(I\cup U_S)\): map \(J\) to \(J\setminus I\), or adjoin \(I\) in the reverse direction. Inclusion–exclusion therefore yields
\[\sum_{S\subseteq\operatorname{Max}(I)}(-1)^{|S|}\mathcal D\bigl(B_n\setminus(I\cup U_S)\bigr)\]
for ideals \(J\supseteq I\) passing all frontier requirements. Here \(J=I\) cannot pass any frontier requirement because every nonempty proper \(I\) has a maximal element with at least one cover. The single ideal \(J=B_n\) always passes but makes \(f\) omit \(2\), so subtract exactly one. Summing over \(I\) gives the exact formula
\[\boxed{F_n=\sum_{\substack{I\text{ a downset of }B_n\\\varnothing\ne I\ne B_n}}\left[\sum_{S\subseteq\operatorname{Max}(I)}(-1)^{|S|}\mathcal D\bigl(B_n\setminus(I\cup U_S)\bigr)-1\right].}\]

**4. Existence.** For \(n\le1\), the source has fewer than three worlds. For \(n\ge2\), the map \(f(x)=\min(|x|,2)\) is monotone onto and satisfies the frontier condition, so \(F_n>0\).

**5. Exact small counts.** The counts above follow by exhaustive enumeration of all downsets \(I,J\) in independent code and, separately, from every monotone ternary assignment on the 32 Boolean worlds. The two methods agree through \(n=5\). A third direct implementation of the inclusion–exclusion formula agrees for \(n\le3\). These computations justify the displayed finite values, not the all-parameter proof, which was established separately.

## Verification
Run with any C++17 compiler and Python 3, from the directory containing the verification files:

```sh
g++ -O2 -std=c++17 verification/ideal_pairs.cpp -o ideal_pairs
./ideal_pairs
g++ -O2 -std=c++17 verification/direct_ternary.cpp -o direct_ternary
for n in 1 2 3 4 5; do ./direct_ternary "$n"; done
python3 verification/verify_ie.py
```

Both C++ programs enumerate exact integers with no floating-point computation. The first generates all \(7{,}581\) downsets of \(B_5\) and tests pairs; the second independently generates every order-preserving assignment of \(0,1,2\) and tests back-lifting directly for each zero-valued world. The latter sees \(7{,}805{,}614\) onto monotone assignments and retains \(3{,}242{,}450\). Python verifies the induced-poset downset inclusion–exclusion through \(n=3\). Included logs provide the expected outputs.

## Relationship to prior work
Bounded morphisms (also called \(p\)-morphisms) and their modal validity properties are standard; the basic forth/back definition is recorded in the PlanetMath article *p-morphism*. Frank a Campo, *A recursive approach for the enumeration of the homomorphisms from a poset P to the chain C3* (2021), develops exact counts for **all order-preserving** maps into a three-point chain, using order polynomials and downset recursions. Those broader counts do not impose the back-lifting requirement and do not give the present restricted numbers. Jacqueline Daykin's earlier thesis *Monotonic functions of finite posets* (1984) similarly studies monotone finite-poset maps, including chain targets; its accessible abstract does not establish a bounded-morphism count. The present result distinguishes an order-preserving map from an onto bounded morphism and gives a concrete exact modal-quotient enumeration for the Boolean family.

## Limitations
The inclusion–exclusion expression is finite and exact for all \(n\), but is not claimed to have polynomial computational complexity or to be a closed product formula. The enumerated numerical values stop at \(n=5\); no value for \(n\ge6\) has been calculated here. The map counts are labelled, not quotiented by automorphisms. A literature search cannot establish absolute publication priority; possible unexamined specialist results on open maps between finite posets remain a risk. No independent audit of the result has been performed.

## References
1. *p-morphism*, PlanetMath, created 2013-03-22, https://planetmath.org/pmorphism.
2. Frank a Campo, *A recursive approach for the enumeration of the homomorphisms from a poset P to the chain C3*, arXiv:2104.03079 (2021), https://arxiv.org/abs/2104.03079.
3. Jacqueline Daykin, *Monotonic functions of finite posets*, PhD thesis, University of Warwick (1984), https://wrap.warwick.ac.uk/id/eprint/131009/.
