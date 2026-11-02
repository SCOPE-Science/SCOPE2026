# Fibonacci fibers and the uniquely dominant Lucas basin for odd-ring Rule 5

## Finding

Let \(n\ge3\) be odd, let the vertices of the undirected simple cycle \(C_n\) be \(\mathbb Z/n\mathbb Z\), and define the synchronous open-neighborhood NOR cellular automaton
\[
F(x)_i=(1-x_{i-1})(1-x_{i+1}),\qquad x\in\{0,1\}^n.
\]
For any proposed output \(y\), write \(y'_j=y_{2j\bmod n}\). Let \(f_0=0\), \(f_1=1\), \(f_{k+2}=f_{k+1}+f_k\), and \(\ell_n=f_{n-1}+f_{n+1}\). The number \(p_n(y)=|F^{-1}(y)|\) of labelled one-step predecessors is exactly
\[
p_n(y)=\begin{cases}
\ell_n,&y=0^n,\\
1,&y=1^n,\\
0,&0<\sum_i y_i<n\text{ and a cyclic zero run in }y'\text{ has length }1,\\
\displaystyle\prod_{R}f_{|R|-1},&\text{otherwise,}
\end{cases}
\]
where the final product ranges over the maximal cyclic zero runs in \(y'\). In particular, an output is attainable precisely when its step-two ordering has no isolated zero (the constant cases are attainable).

Every input enters a fixed point or a two-cycle after **one update**. The exact full basin of a fixed point \(y\) is \(p_n(y)\); the exact full basin of a primitive two-cycle \(\{y,F(y)\}\) is \(p_n(y)+p_n(F(y))\). Thus the displayed formula evaluates **every individual attraction basin**, without enumerating the \(2^n\) initial states.

The alternating-in-time orbit \(\{0^n,1^n\}\) is the **unique** attractor of largest basin. Its exact basin is \(\ell_n+1\), while every other attractor has basin at most \(2f_{n-2}<\ell_n+1\). For independently uniformly chosen initial bits, its attraction probability is \((\ell_n+1)/2^n\), asymptotic to \((\varphi/2)^n\), with \(\varphi=(1+\sqrt5)/2\).

For completeness, the already-understood recurrent-state census can be expressed using the Perrin numbers \(P_0=3\), \(P_1=0\), \(P_2=2\), \(P_k=P_{k-2}+P_{k-3}\): the number of recurrent states is \(P_{2n}\), of fixed points \(P_n\), and of primitive two-cycle orbits \((P_{2n}-P_n)/2\). **The novelty claim does not include the general Rule-5 update identity, the classical preimage-recursion method, or the known isolated-symbol cyclic-word census.**

## Assumptions and scope

The graph is a labelled, undirected, loopless cycle of odd length at least three. All sites update simultaneously using only their two distinct neighbors and not their own previous state. Binary arithmetic is ordinary integer arithmetic on \(\{0,1\}\). Time is the number of complete simultaneous updates. A basin includes the attractor's periodic states. Fibonacci, Lucas, and Perrin sequences are normalized exactly as above; the empty cyclic-run product only occurs in a constant word and is handled separately. No assertion is made for even cycle lengths, other Boolean local rules, or stochastic updates.

## Proof

**1. Every image state is periodic, with period dividing two.** For any finite simple undirected graph, its open-neighborhood NOR map \(F\) is antitone in the coordinate order. Moreover \(x\le F^2(x)\): if \(x_v=1\), every neighbor of \(v\) has value zero in \(F(x)\), hence \(F^2(x)_v=1\). Antitonicity gives \(F^3(x)\le F(x)\); applying \(x\le F^2(x)\) to \(F(x)\) gives \(F(x)\le F^3(x)\). Therefore \(F^3=F\). On the image, \(F^2\) is the identity; all image states are recurrent, and every input reaches one in at most one step. This general observation is background, not a new assertion about arbitrary graphs.

**2. Reduction to adjacent-AND constraints on an odd cyclic word.** Since \(\gcd(2,n)=1\), the map \(j\mapsto2j\bmod n\) permutes the vertices. Define \(z_j=1-x_{2j-1\bmod n}\). Then
\[
y'_j=F(x)_{2j}=(1-x_{2j-1})(1-x_{2j+1})=z_jz_{j+1}.
\]
The change from \(x\) to \(z\) is bijective. Thus every predecessor is counted exactly once by a cyclic binary assignment with prescribed neighboring products.

**3. Solution of each inverse fiber.** If \(y'=1^n\), each adjacent product equals one, forcing \(z=1^n\) and giving one predecessor. If \(y'=0^n\), the \(z\)-word has no adjacent ones on a cycle. Its count is the Lucas number \(f_{n-1}+f_{n+1}\), by splitting according to a fixed vertex being zero or one and counting the remaining path independent sets.

Otherwise consider a maximal cyclic zero run of length \(L\) between two positive output edges. The output-one edges force the two pairs of their endpoint \(z\)-bits to one. A zero run of length one is impossible, since its two endpoints are then forced to one. For \(L\ge2\), the bits immediately inside the zero-run boundary edges are forced zero; the remaining \(L-3\) possible interior positions (when positive) are free except that they must contain no adjacent ones. A path of \(m\) positions has \(f_{m+2}\) independent sets, hence there are \(f_{L-1}\) choices. This also gives one choice for \(L=2\) and \(L=3\) directly. Distinct runs involve disjoint unforced positions, so their counts multiply. This proves the fiber formula and the image criterion.

**4. Basin formula and maximality.** Because \(F^3=F\), the sets \(F^{-1}(y)\) for states \(y\) in one fixed or two-cycle partition its entire basin. Hence the stated basin formulas follow without double counting.

For a nonconstant attainable \(y\), let \(r\le n-1\) be the number of zeros of \(y'\), arranged in \(k\ge1\) runs of lengths \(L_1,\ldots,L_k\ge2\). The Fibonacci addition identity gives \(f_af_b\le f_{a+b-1}\) for all positive integers \(a,b\); induction yields
\[
p_n(y)=\prod_{j=1}^{k}f_{L_j-1}\le f_{\sum_j(L_j-1)-(k-1)}=f_{r-2k+1}\le f_{n-2}.
\]
The all-ones output has only one predecessor and satisfies the same bound. The only other output with \(\ell_n\) predecessors is the all-zero output, and its forward partner is all ones. Every other fixed point has a basin of at most \(f_{n-2}\); every other two-cycle at most \(2f_{n-2}\). For every odd \(n\ge3\), \(2f_{n-2}<f_{n-1}+f_{n+1}+1\). This proves uniqueness and the exact basin maximum.

**5. Known census and asymptotic.** A fixed state is precisely an indicator of a maximal independent vertex set of \(C_n\), counted by \(P_n\). By step 3, image states correspond to cyclic binary words without cyclic occurrence of \(101\) in the step-two order. The transfer matrix on adjacent symbol pairs \(00,01,10,11\) is
\[
M=\begin{pmatrix}1&1&0&0\\0&0&1&1\\1&0&0&0\\0&0&1&1\end{pmatrix}.
\]
Its characteristic polynomial is \(\lambda(\lambda^3-2\lambda^2+\lambda-1)\). The count \(\operatorname{tr}(M^n)\) satisfies that order-three recurrence and agrees in its first three positive indices with \(P_{2n}\), hence is \(P_{2n}\) for every \(n\ge1\). Since the image consists solely of periods one and two, the two-cycle count follows. These census identities are included to place the individual-basin theorem in context; the isolated-symbol word-count sequence was previously tabulated. Finally \(\ell_n=\varphi^n+(-\varphi)^{-n}\), so \((\ell_n+1)/2^n\sim(\varphi/2)^n\).

## Verification

The separate `verify_python.py` and `verify_cpp.cpp` programs implement the update rule independently. The Python program enumerates all \(2^n\) initial configurations for every odd \(n\) from \(3\) to \(19\), compares all individual output-fiber counts with the proposed formula, then checks the periodic census and unique maximal basin. The C++ program repeats the complete fiber and orbit checks for every odd \(n\) from \(3\) to \(21\), including all \(2{,}097{,}152\) states at \(n=21\). Outputs are embedded as `verify_python_output.txt` and `verify_cpp_output.txt`. These are finite cross-checks, **not** replacements for the uniform proof in section 3.

Reproduce by running `python3 verify_python.py` and by compiling and running `c++ -std=c++17 -O2 verify_cpp.cpp -o check && ./check` in a directory containing the four named verification artifacts. The program output is deterministic.

## Relationship to prior work

The update is exactly Wolfram's elementary cellular automaton **Rule 5**: the central bit is ignored and a new one is produced when both neighboring bits are zero. The explicit alternating one-step/two-step formula for Rule 5 is recorded in Henryk Fukś's solvable-automata compilation, so short eventual period is not claimed new. Erica Jen's 1988 cylindrical-cellular-automata work already studies periodic states and counts for general periodic rings. Jen's 1989 study gives general one-step preimage recurrences on infinite lattices, with Rule 5 in a recurrence category; Fukś (2003, arXiv version 2013) counts iterative preimages of small cylinder blocks. These supply methods and background but do not state, in the material inspected, the odd-ring **individual cyclic fiber product and full basin ranking**. The cyclic binary-word count lacking an isolated symbol is also recorded at OEIS A109377, first dated August 25, 2005; no originality is assigned to the total image-state count. Earlier classifications of open-NOR on bipartite graphs and other graph families also do not imply the odd-cycle run-factorization because the step-two permutation is connected on odd cycles rather than splitting parity classes.

## Limitations

The finding is an exact statement for odd finite rings only; the formula does not extend unchanged to even rings. The broader Rule-5 evolution law, transfer-matrix methods, and the cyclic-word count were known. Jen (1988), a closely relevant source for periodic ring attractors, was accessible only through its abstract, not its full text, in this investigation; previously unindexed treatments of cyclic preimage fibers or Rule-5 basins could contain an equivalent result. The recurrence method of Jen (1989) can be specialized to individual rules, so priority is claimed only for the explicitly evaluated cyclic product and resulting complete basin comparison. No independent audit or historical uniqueness certification has been performed.

## References

1. E. Jen, “Cylindrical cellular automata,” *Communications in Mathematical Physics* **118** (1988), 569–590, doi:10.1007/BF01221109. Only its public abstract was available for direct inspection.
2. E. Jen, “Enumeration of Preimages in Cellular Automata,” *Complex Systems* **3** (1989), 421–456, https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf .
3. H. Fukś, “Sequences of Preimages in Elementary Cellular Automata,” *Complex Systems* **14** (2003), 29–43; public preprint https://arxiv.org/abs/1305.6533 .
4. H. Fukś, “Deterministic solution formulae for elementary CA rules,” https://lie.ac.brocku.ca/~hfuks/solvableca.html (Rule 5 entry).
5. OEIS Foundation, A109377, https://oeis.org/A109377 (cyclic words without isolated symbols; first recorded 2005-08-25).
