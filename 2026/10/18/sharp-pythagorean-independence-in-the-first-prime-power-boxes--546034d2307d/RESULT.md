# Sharp Pythagorean independence in the first prime-power boxes

## Finding

Let \(p_1<p_2<\cdots\) be the increasing primes and, for every integer \(N\ge1\), define
\[
\Phi_N=\left\{\prod_{j=1}^{N}p_j^{a_j}:a_j\in\{0,1,\ldots,N-1\}\right\}.
\]
The Pythagorean-leg conflict graph \(G_N\) has vertex set \(\Phi_N\) and an edge between **distinct** vertices \(u,v\) exactly when \(u^2+v^2\) is an integer square. Its independence number is the prime-box extremal quantity \(f(N)\) introduced by Xiao.

**Theorem.** The first four exact values are
\[
\boxed{f(1)=1,\quad f(2)=4,\quad f(3)=21,\quad f(4)=144.}
\]
Moreover, \(G_N\) is bipartite **if and only if** \(1\le N\le4\). A triangle already occurs in \(G_5\), on the vertices \(240,252,275\), and persists in every \(G_N\) with \(N\ge5\).

## Assumptions and scope

All vertices are positive integers; the hypotenuse may lie outside the box. The integer \(N\) ranges over **all** positive integers for the bipartiteness theorem, and \(1\le N\le4\) for the exact independence numbers. No independence number is claimed for \(N\ge5\). This uses the exact prime-power boxes and the *two-leg* exclusion in Xiao's definition, not exclusion of complete triples within a set.

## Proof

**1. Valuation obstruction.** For any integer Pythagorean triple \(u^2+v^2=w^2\), dividing through by \(\gcd(u,v)\) gives coprime positive legs. They cannot both be odd (their squared sum is \(2\pmod{4}\)), and in the primitive triple the even leg must be divisible by \(4\): otherwise its square and the odd square sum to \(5\pmod{8}\), which is not a square. Thus, whenever \(\{u,v\}\) is an edge,
\[
\boxed{|\nu_2(u)-\nu_2(v)|\ge2.}
\]
For \(N\le4\), all vertex valuations belong to \(\{0,\ldots,N-1\}\subseteq\{0,1,2,3\}\). The two classes \(\nu_2\in\{0,1\}\) and \(\nu_2\in\{2,3\}\) therefore form a bipartition: every edge joins the two classes. For \(N=1,2\), the graph has no edges at all.

**2. Sharp finite extremal certificates.** For each \(N\in\{3,4\}\), the supplied `certificates.json` lists an independent vertex set \(I_N\) and a family \(M_N\) of vertex-disjoint edges in \(G_N\). Exact exhaustive pair generation from the definition, independently checked by `verify.py`, gives:

| \(N\) | \(|\Phi_N|\) | Edges | \(|M_N|\) | \(|I_N|\) |
| ---: | ---: | ---: | ---: | ---: |
| 3 | 27 | 10 | 6 | 21 |
| 4 | 256 | 408 | 112 | 144 |

Any independent set contains at most one endpoint of each disjoint edge, hence its cardinality is at most \(|\Phi_N|-|M_N|\). Every listed member of \(I_N\) belongs to \(\Phi_N\), and no two listed members are adjacent. Therefore \(f(3)=27-6=21\) and \(f(4)=256-112=144\). The cases \(N=1,2\) follow from the edgeless graph and \(|\Phi_N|=N^N\). This is a **complete finite proof**: the verifier checks every distinct vertex pair, all matching edges, endpoint disjointness, and every potential edge internal to the independent set. It does not infer extremality from a heuristic solver or from a partial search.

For additional independent edge-enumeration evidence, the primitive positive leg ratios in \(G_3\) are \(3:4\) (six edges) and \(5:12\) (four edges). In \(G_4\) the complete ratio table is \(3:4\) (96), \(5:12\) (72), \(12:35\) (54), \(20:21\) (54), \(7:24\) (36), \(8:15\) (36), \(28:45\) (36), and \(9:40\) (24), totaling \(408\) edges. All fractions in this table name reduced leg pairs, not hypotenuse restrictions.

**3. Sharp loss of bipartiteness.** The three vertices
\[
240=2^4\cdot3\cdot5,\qquad252=2^2\cdot3^2\cdot7,\qquad275=5^2\cdot11
\]
all lie in \(\Phi_5\), and
\[
240^2+252^2=348^2,\quad240^2+275^2=365^2,\quad252^2+275^2=373^2.
\]
Hence they form a triangle, so \(G_5\) is not bipartite. Since \(\Phi_5\subseteq\Phi_N\) for every \(N\ge5\), this same triangle appears in every larger graph. Together with Step 1, bipartiteness holds exactly through \(N=4\). The three side lengths form a *previously known* Euler brick; the brick itself is not claimed as a discovery.

## Verification

Run `python3 verify.py` next to `certificates.json` with Python 3 standard library only. It regenerates all \(27\) and \(256\) box vertices, checks all \(351\) and \(32640\) unordered pairs, respectively, checks the exact primitive-leg ratio multiplicities and the disjoint-edge and independent-set certificates, and verifies the three displayed Pythagorean identities for the triangle in \(\Phi_5\). Expected final line:

`PASS: f(1)=1, f(2)=4, f(3)=21, f(4)=144; triangle at n=5`

No numerical approximation, randomized algorithm, or unverified external mathematical oracle is required. The explicit matching and independent-set witnesses, rather than the software that found them, certify the finite claims.

## Relationship to prior work

Rongzhong Xiao's October 8, 2026 preprint defines exactly the same \(\Phi_N\) and \(f(N)\) and proves an asymptotic decay estimate \(f(N)\ll N^N(\log\log N)^{-1/1296}\), with a nonexplicit threshold. Its stated results do not give these small-box exact values or the bipartiteness transition. The earlier partition-regularity theorem of Frantzikinakis, Klurman and Moreira concerns finite colorings and positive multiplicative density, and does not imply these finite cardinalities. The triple \((240,252,275)\) is a classical Euler-brick example; the claim is its position at the sharp first nonbipartite **prime-box** parameter, not novelty of the triple.

## Limitations

The exact finite census stops at \(N=4\). The triangle at \(N=5\) proves failure of bipartiteness but does not determine \(f(5)\), later independence numbers, or an improved asymptotic bound. The result does not certify absence of every unindexed or unpublished equivalent computation. Its numerical equalities are backed by exhaustive finite certificates rather than by a parameter-uniform closed formula for \(f(N)\).

## References

1. Rongzhong Xiao, *Pythagorean pairs in boxes of prime powers*, arXiv:2610.11965v1, first posted 2026-10-08, Sections 1.2 and 8.4, https://arxiv.org/abs/2610.11965.
2. N. Frantzikinakis, O. Klurman and J. Moreira, *Partition regularity of Pythagorean pairs*, Forum of Mathematics, Pi 13 (2025), e5; arXiv:2309.10636v5, https://arxiv.org/abs/2309.10636.
3. Wolfram MathWorld, *Euler Brick*, https://mathworld.wolfram.com/EulerBrick.html (lists the previously known triple with side lengths \(240,252,275\)).
