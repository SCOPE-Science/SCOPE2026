# Exact universal-word probability after three binary factor deletions

## Finding

For every integer \(n\ge4\), independently select three distinct length-\(n\) binary words and delete them from \(\{0,1\}^n\). Exactly
\[
10\cdot2^n-56
\]
of the \(\binom{2^n}{3}\) three-element deletion sets leave a family possessing a **linear universal word**: a binary word in which every surviving length-\(n\) block occurs exactly once, with no other length-\(n\) blocks. Consequently the exact probability of existence is
\[
P_{\mathrm w}(n,2,3)=\frac{10\cdot2^n-56}{\binom{2^n}{3}}\qquad(n\ge4).
\]
There are exactly \(10\cdot2^n-46\) deletion triples satisfying the necessary directed Euler-trail degree conditions, and precisely ten of these fail the active-vertex connectivity condition. This separation describes every obstruction.

## Assumptions and scope

The alphabet is the *labeled* binary set \(\{0,1\}\). Deletion sets consist of **three distinct** words, each length \(n\). A linear universal word for the retained set is a word of length \(2^n+n-4\) whose \(2^n-3\) consecutive, overlapping length-\(n\) factors are exactly the retained words, once each. No cyclic wraparound is allowed. Our theorem starts at \(n=4\); it makes no claim for smaller lengths or nonbinary alphabets.

Put \(m=n-1\) and \(N=2^n\). Let \(D=B(2,m)\) be the binary de Bruijn digraph with vertices \(\{0,1\}^m\) and one labeled arc \(x_1\cdots x_m b\) from \(x_1\cdots x_m\) to \(x_2\cdots x_m b\) for each binary word of length \(n\). It has \(N\) arcs, two incoming and two outgoing at each vertex. A deleted word means its corresponding arc is deleted. Degree conditions and connectivity always concern the residual directed multigraph; vertices carrying no surviving arc are ignored.

## Proof

**1. Exact correspondence.** Reading successive overlapping length-\(n\) factors of a linear word traces a directed trail through \(D\), using each retained arc exactly once. Conversely, an Euler trail in the residual digraph spells the required linear universal word. The directed Euler-trail criterion is: all vertices incident with retained arcs lie in one weak component, and the outdegree-minus-indegree vector is either identically zero or equals \(+1\) at one vertex and \(-1\) at another. Since \(D\) is balanced, negating the deleted-arc divergence has the same admissible patterns.

**2. Count deleted triples satisfying the degree criterion.** Of the \(N\) arcs, exactly two are loops, exactly two form the unique directed two-cycle, and exactly six form the two distinct directed three-cycles. These are elementary consequences of primitive binary necklaces of periods one, two and three.

An admissible deletion triple with zero divergence is a union of directed cycles. Since three arcs are deleted, the only possibilities are one loop together with the two-cycle (two choices), or one of the two three-cycles (two choices), giving \(4\) balanced triples.

All remaining degree-admissible triples have divergence \(+1\) at one vertex and \(-1\) at another. Classify by loops and presence of the two-cycle:

- Both loops, plus any other nonloop arc: \(N-2\) triples.
- The full two-cycle, plus a further nonloop arc: \(N-4\) triples.
- Exactly one loop, without the full two-cycle: the other two arcs form an open directed two-edge trail. There are \(2N\) ordered two-edge walks, of which \(6\) use a loop and \(2\) traverse the two-cycle. Each remaining two-edge trail represents one unordered edge pair; multiplying \(2N-8\) by two loop choices yields \(4N-16\) triples.
- No loop and no full two-cycle: all three arcs form a directed open three-edge trail, not a directed three-cycle. There are \(4N\) ordered three-edge walks. Exactly \(16\) contain a loop (inclusion-exclusion over the three positions); exactly \(6\) loop-free walks contain consecutive opposite arcs forming the two-cycle (including the two repeated-arc walks); and exactly \(6\) remaining walks traverse a directed three-cycle. The remaining \(4N-28\) walks contain three distinct arcs, admit a unique Euler-trail ordering, and represent \(4N-28\) triples.

For completeness, the unique-ordering assertion follows because a three-edge Euler trail with no loop, two-cycle or directed three-cycle cannot have a repeated vertex: a repeat at distance one, two or three would create respectively a loop, a directed two-cycle or a directed three-cycle. A balanced component of a disconnected three-edge deletion set must itself be a directed cycle; without loops/two-cycles this would consume all three arcs and force the balanced case. Thus the above list exhausts the unbalanced degree-admissible triples. Adding the four cases and the four balanced triples gives
\[
(N-2)+(N-4)+(4N-16)+(4N-28)+4=10N-46.
\]

**3. The only connectivity failures.** For any nonempty proper set of vertices \(S\) of the original balanced graph \(D\), the number of arcs leaving \(S\) equals the number entering. If deleting at most three arcs disconnects the *underlying undirected* graph into active components, take the vertex set of one such component. The cut has lost every crossing arc; thus both original directed cut counts were at most one. The super-edge-connectivity theorem for de Bruijn digraphs \(B(d,m)\), valid for \(d\ge2,m\ge1\) (Xu and Lü, 2008, Corollary 1), forces a directed cut of size one to isolate a vertex. Its only possible singleton here is a constant vertex \(a^m\), because a nonconstant vertex has two distinct outgoing and two distinct incoming external arcs. An isolated nonconstant vertex would require removing all four of its incident arcs, impossible with three deletions. Therefore every connectivity failure under consideration leaves a constant vertex with its loop as an active isolated component.

For either \(a\in\{0,1\}\), write \(b=1-a\), and let \(A=a^m\), \(B=a^{m-1}b\), \(C=ba^{m-1}\). Exactly two external arcs touch \(A\): the outgoing arc \(A\to B\) labeled \(a^m b\), and the incoming arc \(C\to A\) labeled \(ba^m\). Both must belong to any disconnected triple. These two deleted arcs have combined deleted divergence \(+1\) at \(C\) and \(-1\) at \(B\), with \(B\ne C\). For the third deleted arc to preserve the degree criterion, it must be a loop, an arc leaving \(B\), or an arc entering \(C\). The two loops and these four arcs are all distinct when \(m\ge3\); the possible arc \(B\to C\) does not exist. There are exactly six choices. The loop at \(A\) is the sole non-obstructing choice, since removing it makes \(A\) inactive. Each of the other five leaves an active isolated component, hence fails.

The two constant vertices give disjoint failure families, so exactly \(2\cdot5=10\) degree-admissible deletion triples are non-realizable. Subtracting them from \(10N-46\) proves \(10N-56\). The formula for the probability follows by uniform choice among \(\binom N3\) triples. \(\square\)

## Verification

The accompanying `verify.py` (Python standard library only) independently enumerates all three-element deletion sets for \(n=4,5,6,7\), constructs the corresponding residual de Bruijn graph from first principles, tests Euler divergence and active-vertex weak connectivity, and checks every of the six combinatorial classes plus the ten predicted failures. Execute `python verify.py`. The exact successful counts are \(104,264,584,1224\), with degree-admissible counts \(114,274,594,1234\) respectively. This finite experiment is a consistency check, **not** the proof of the infinite assertion; the proof is the preceding classification and the published super-edge-connectivity theorem.

## Relationship to prior work

Chen, Kitaev and Sun (first public 2019-08-03) introduced precisely the probabilities \(P_{\mathrm c}(n,k,s)\) and \(P_{\mathrm w}(n,k,s)\) for deleted words. Their preprint gives exact cases for \(s\le2\), a finite table at binary \(n\le4\), and general lower bounds. Its binary \(n=4,s=3\) entry is \(13/70\), agreeing with \(104/560\) here, but does not imply the all-\(n\) formula. The present result enumerates *linear Euler trails after three arc deletions*, unlike cyclic Euler circuits: their degree requirements and counts differ.

Xu and Lü (2008) established super-edge-connectivity of the de Bruijn digraph, used above only to rule out other three-arc disconnections. This known graph theorem is not claimed as new.

## Limitations

The exact statement requires \(n\ge4\), binary alphabet, three *distinct* forbidden length-\(n\) factors, and exact-once **linear** coverage. There is no claim about the number of universal words per deletion set, cyclic coverage, longer deletion sets, or larger alphabets. Published equivalences under other terminology might have escaped the literature search; novelty is subject to independent assessment.

## References

1. H. Z. Q. Chen, S. Kitaev and B. Y. Sun, *On the probability of existence of a universal cycle or a universal word for a set of words*, arXiv:1908.01116 (first posted 2019-08-03), https://arxiv.org/abs/1908.01116 ; journal version *Mathematics* **8** (2020), 778, https://doi.org/10.3390/math8050778 .
2. J.-M. Xu and M. Lü, *Restricted Edge-Connectivity of de Bruijn Digraphs*, *Ars Combinatoria* **87** (2008), 385–392, https://combinatorialpress.com/article/ars/Volume%20087/volume-87-paper-30.pdf .
