# Strong sync-maximality equals primitivity in degree \(5\)
## Finding
For permutation groups of degree \(5\),
\[
G\text{ is strongly sync-maximal}
\quad\Longleftrightarrow\quad
G\text{ is primitive}.
\]

The substantive finite core is that the regular cyclic group
\[
C_5=\langle c\rangle,\qquad c=(0\,1\,2\,3\,4),
\]
is itself strongly sync-maximal.

More quantitatively, for every transformation
\[
f:\{0,1,2,3,4\}\to\{0,1,2,3,4\}
\]
of rank \(2\), \(3\), or \(4\), and every two distinct \(2\)-subsets \(S,T\), there is a word over the two transformations \(c,f\) of length at most \(9\) that maps exactly one of \(S,T\) to a singleton. The bound \(9\) is sharp: among all \(3000\cdot45=135000\) map/pair instances, exactly \(10\) have shortest distinguishing length \(9\).

## Assumptions and scope
A permutation group \(G\le S_n\) is strongly sync-maximal if, for every transformation \(f\) of rank
\[
2\le \operatorname{rank}(f)\le n-1,
\]
all distinct \(2\)-subsets are distinguishable in the transformation monoid
\[
\langle G\cup\{f\}\rangle.
\]
Two subsets are distinguishable when some generated transformation maps precisely one of them to a singleton.

The classification concerns degree \(5\) only. The finite verification establishes the strong property for the cyclic subgroup \(C_5\); the passage from \(C_5\) to every primitive degree-\(5\) group is then a short group-theoretic argument.

## Proof
First prove that \(C_5\) is strongly sync-maximal.

There are exactly
\[
5^5-5!-5=3000
\]
transformations of ranks \(2\), \(3\), or \(4\) on five points: \(300\) of rank \(2\), \(1500\) of rank \(3\), and \(1200\) of rank \(4\). There are
\[
\binom{\binom52}{2}=45
\]
unordered pairs of distinct \(2\)-subsets.

For every admissible \(f\) and every such pair \((S,T)\), form the finite directed state graph whose states are ordered pairs \((X,Y)\) of nonempty subsets of the five-point set and whose two transitions apply \(c\) or \(f\) simultaneously to both components. The target states are exactly those for which one component is a singleton and the other is not.

An exhaustive reverse breadth-first search from all target states reaches every one of the \(135000\) initial map/pair instances. Thus every pair of \(2\)-subsets is distinguishable in \(\langle C_5,f\rangle\) for every permitted \(f\), which is precisely strong sync-maximality of \(C_5\).

The exact distribution of shortest distinguishing lengths over the \(135000\) instances is
\[
\begin{array}{c|rrrrrrrrr}
\ell&1&2&3&4&5&6&7&8&9\\ \hline
N_\ell&
45000&42360&28420&13525&4395&1005&235&50&10.
\end{array}
\]
In particular the universal bound \(9\) is exact.

Now let \(G\) be any primitive permutation group of degree \(5\). Such a group is transitive. By orbit-stabilizer, \(5\) divides \(|G|\), so Cauchy's theorem gives an element of order \(5\). In degree \(5\), an element of order \(5\) is a \(5\)-cycle. Hence \(G\) contains a conjugate of \(C_5\).

Strong sync-maximality is upward monotone in the permutation group: if \(H\le G\) is strongly sync-maximal, then for every admissible \(f\),
\[
\langle H,f\rangle\subseteq\langle G,f\rangle,
\]
so every distinguishing transformation available for \(H\) is also available for \(G\). Since every primitive degree-\(5\) group contains a cyclic \(5\)-cycle subgroup and \(C_5\) is strongly sync-maximal, every primitive degree-\(5\) group is strongly sync-maximal.

Conversely, Hoffmann proves that every strongly sync-maximal permutation group is primitive. This gives the equivalence.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The first engine checks all \(3000\) admissible transformations without symmetry reduction. For each map it constructs the complete ordered-pair subset transition graph under \(c\) and \(f\), runs reverse breadth-first search from all distinguishing states, and obtains exact shortest distances for all \(45\) pairs of distinct \(2\)-subsets.

The second engine is independent in organization. It quotients transformations by
\[
f\sim c^a f c^b,
\]
which does not change the monoid generated together with \(c\). This gives exactly \(12\), \(60\), and \(48\) representatives in ranks \(2\), \(3\), and \(4\). Simultaneous cyclic rotation gives exactly \(9\) orbits of distinct \(2\)-subset pairs. For every one of the \(120\) transformation representatives, the verifier explicitly generates the full transformation monoid and scans it for a distinguishing element for each pair-orbit representative.

Both engines establish the same universal strong property; the first additionally certifies the sharp length-\(9\) bound.

## Relationship to prior work
Hoffmann introduced strong sync-maximality as a stronger variant after proving that ordinary sync-maximal permutation groups are exactly the primitive groups. The paper proves
\[
\text{\(4\)-transitive}\Longrightarrow
\text{strongly sync-maximal}\Longrightarrow
\text{primitive}
\]
and explicitly states that whether the strong class is properly contained between the surrounding classes is open.

The degree-\(5\) classification above is not implied by the \(4\)-transitivity sufficient condition: the cyclic group \(C_5\) is regular, hence very far from \(4\)-transitive. The result shows that at degree \(5\), the stronger condition already holds for the smallest possible transitive subgroup and therefore for every primitive group.

Targeted searches for strong sync-maximality together with degree \(5\), \(C_5\), cyclic groups, prime degree, and the five-point primitive-group classification did not locate a published covering statement. Later work on primitive automata and completely distinguishable automata studies neighboring synchronization notions but does not state this degree-\(5\) strong-group classification.

## Limitations
The theorem is specific to degree \(5\). It does not assert that cyclic groups of arbitrary prime degree are strongly sync-maximal, nor that strong sync-maximality equals primitivity in higher degrees.

The proof that \(C_5\) is strong is a complete finite verification rather than a uniform prime-degree argument. The quantitative bound \(9\) is likewise specific to the generator \(c\) in degree \(5\).

An unindexed note or unpublished small-degree computation could contain the same classification.

## References
1. S. Hoffmann, “Sync-Maximal Permutation Groups Equal Primitive Permutation Groups,” arXiv:2111.13527v1, first public version 2021-11-26; DCFS 2021, DOI 10.1007/978-3-030-93489-7_4.
2. I. Rystsov and M. Szykuła, “Primitive Automata that are Synchronizing,” arXiv:2307.01302v1, first public version 2023-07-03.
