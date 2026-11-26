# Independent mathematical audit

## correctness

PASS

A length-L word is specified by its initial bit and zero, one or two change locations; constant extension realizes each and the count is L²−L+2. At any fixed observation scale, uniform continuity of the quotient gives a word radius R. Equal unordered sets of words on [−R,N−1+R] give small Hausdorff orbit distance in both directions, even if representative multiplicities differ. Thus s_N=O(N^(2n)), and a continuous factor gives the same upper bound after singleton collapse. For a matching lower bound, use 2n successive windows of lengths proportional to N on one coarse grid of spacing larger than the fixed observation radius, pair successive windows for the two transitions of each finite 1-block, and choose one time in each window. At a differing passage time one configuration has a step marker separated from p and the other has only points near p. Every nonpassing point in the first configuration is also near p. For n≥2 the passing configuration is near {p,u} or {p,v}, whose suspension images are distinct from the collapsed singleton point. Uniform continuity supplies a fixed positive separation after collapse. This produces Ω(N^(2n)) choices at a fixed scale and handles n=1 before collapse. Closed inclusion of each F_n in the full hyperspace gives infinite polynomial entropy there; the finite-layer bound gives zero topological entropy at every scale. The recurrent context also checks independently: all nonconstant points are homoclinic to p and admit a transition cylinder that never returns (a specified transition type can occur only once); pseudo-orbits can jump between their two tails near p. Pairs of opposite steps are nonwandering in F_2: approximate each by a long block that first displays the designated step and then, at a common late time, displays the opposite member's step. The unordered pair returns arbitrarily near itself. Varying their locations gives infinitely many such configurations.

## originality

PASS

Best of current knowledge for exact 2n growth on this identified two-transition system, particularly the fixed-scale lower bound that survives singleton collapse. The construction and its recurrence properties are established. The inspected multiplicative entropy theorem assumes finite chain recurrence, while here every point is chain recurrent. The strongest verified general lower bound under wandering with finite limit sets gives n, not 2n. The closest same-system record instead classifies nonwandering finite configurations.

## value

PASS

The same basic test system lies outside the finite-chain-recurrence multiplicativity theorem. Exact entropy at all finite levels, including survival of 2n independently observable passage times after collapse, settles a natural boundary case. It exhibits unbounded polynomial complexity across zero-topological-entropy finite layers. The key significance is the exact growth and robust collapsed-layer detection, not merely applying a factor inequality or calculating word counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
