# The nonsplit integral oriented-line extension of the Fano matroid

## Finding
Let \(P=\mathbb F_2^3\setminus\{0\}\) and let \(K=IN(F_7)\) denote the Fano matroid independence complex. Its vertices are the seven nonzero vectors; every pair and every noncollinear triple is a face. Let \(S\) be the full two-skeleton of the simplex on these seven vertices. The seven triangles missing from \(K\) are exactly the Fano lines \(L=\{a,b,c\}\) with \(a+b+c=0\). Put \(G=GL_3(\mathbb F_2)\), \(W=\ker(\mathbb Z^P\xrightarrow{\mathrm{sum}}\mathbb Z)\), and let \(T=\bigoplus_{L}\bigwedge^3\mathbb Z^L\), with the natural signed permutation action on oriented lines.

**Theorem.** There is a natural short exact sequence of integral \(G\)-modules
\[
0\longrightarrow H_2(K;\mathbb Z)\longrightarrow \bigwedge^3 W
\xrightarrow{\pi}T\longrightarrow 0.
\]
Its three terms are free of ranks \(13,20,7\), and the image of \(H_2(K;\mathbb Z)\) is saturated. The sequence has **exact equivariant splitting exponent four**: the smallest \(m>0\) admitting a \(G\)-linear integral \(s:T\to\bigwedge^3W\) with \(\pi s=m\operatorname{id}_T\) is \(4\). In particular, it has no integral \(G\)-equivariant splitting, although it splits over \(\mathbb Q\) and as a sequence of abelian groups.

The unique reduced nonzero homology of \(K\) is \(\widetilde H_2(K;\mathbb Z)\cong\mathbb Z^{13}\). Its complete complex \(G\)-representation is \(V_7\oplus V_3\oplus\overline{V_3}\), where the subscripts are dimensions and the two three-dimensional summands are conjugate nonisomorphic irreducibles. In the class order \(1A,2A,3A,4A,7A,7B\), the top homology character is
\[
(13,-3,1,1,-1,-1).
\]
The signed line module \(T\otimes\mathbb C\) is the irreducible \(V_7\), rather than the ordinary permutation module on seven lines.

## Assumptions and scope
The assertion uses the standard integral oriented simplicial chain complexes with simplex vertices in increasing order after identifying nonzero binary vectors with \(1,\ldots,7\); binary addition is bitwise XOR. The action of a vertex permutation includes the orientation sign on each oriented simplex. No choice of an orientation of a line is required in the invariant definition of \(T\). The exact exponent refers solely to homomorphisms of \(\mathbb Z[G]\)-modules, not to an extension-order assertion in group cohomology. All groups and maps are as stated, with no asymptotic parameter or unproved infinite extrapolation.

## Proof
**1. The integral exact sequence.** Write \(E=\mathbb Z^P\), with basis indexed by the seven points, and let \(\epsilon:E\to\mathbb Z\) sum the coordinates. The augmented simplicial boundary on \(S\) is contraction with \(\epsilon\). Because the short exact sequence \(0\to W\to E\to\mathbb Z\to0\) splits as abelian groups, its degree-two cycle lattice is canonically \(\ker(\iota_\epsilon:\bigwedge^3E\to\bigwedge^2E)=\bigwedge^3 W\), of rank \(\binom 63=20\). The relative simplicial group \(C_2(S,K)\) is exactly \(T\), and the lower relative chains vanish; thus \(H_2(S,K)\cong T\). The map \(\pi\) takes a cycle to its signed coefficients on the seven missing line triangles.

To prove surjectivity over \(\mathbb Z\), fix a Fano line \(L\) and any point \(x\notin L\). The oriented boundary of the tetrahedron on \(L\cup\{x\}\) lies in \(H_2(S;\mathbb Z)\) and has coefficient \(\pm1\) on \(L\) and zero on every other Fano line: two distinct Fano lines meet in one vertex, hence their union has five vertices. Therefore \(\pi\) is surjective onto all seven oriented line generators. The long exact sequence of the pair \((S,K)\) gives \(H_1(K;\mathbb Z)=0\) and identifies \(H_2(K;\mathbb Z)=\ker\pi\). The rank is \(20-7=13\), and the quotient being free proves saturation. Connectivity and dimension imply all other reduced integral homology groups vanish. The classical matroid-shellability theorem further gives the nonequivariant homotopy type \(K\simeq\bigvee^{13}S^2\), which is established background, not the novelty here.

**2. Rational character.** Each \(g\in G\) permutes the oriented faces. Since reduced homology is supported in degree two, the signed augmented Lefschetz identity gives \(\chi_{H_2}(g)=-1+\operatorname{tr}(g\mid C_0)-\operatorname{tr}(g\mid C_1)+\operatorname{tr}(g\mid C_2(K))\). Enumerating the invertible binary linear maps, whose images of the three basis vectors determine all \(168\) elements, gives the class-size/character pairs \((1,13),(21,-3),(56,1),(42,1),(48,-1)\) grouped by element order \(1,2,3,4,7\). The order-seven part splits into two classes of \(24\) with the same value \(-1\). The signed line character is \((7,-1,1,-1,0,0)\); its squared inner product is \(1\), so it is absolutely irreducible of dimension seven. Comparing the residual character \((6,-2,0,2,-1,-1)\) with the standard \(PSL_2(7)\) table gives \(V_3\oplus\overline{V_3}\). All fixed-simplex signs and class totals are recomputed by the standalone verifier.

**3. Exact obstruction to equivariance over integers.** Fix the oriented line \(L=[1,2,3]\) and its setwise stabilizer \(H\le G\), which has order \(24\). Define \(\eta(h)\) to be the sign of \(h\)'s permutation of the three vertices of \(L\). An equivariant section multiplied by \(m\) would take \([L]\) to an integral two-cycle \(z\) with \(h z=\eta(h)z\) for every \(h\in H\) and with coefficient \(m\) on \([L]\).

The \(H\)-orbits on all \(35\) unordered triples have sizes \(1,12,6,12,4\), represented respectively by \((1,2,3),(1,2,4),(1,4,5),(1,4,6),(4,5,6)\). Integral \(\eta\)-anti-invariant oriented chains can be supported only on the orbits of sizes \(1,12,4\): on each of the other two orbits some setwise stabilizer acts with oriented-simplex sign opposite to \(\eta\), forcing its coefficient to vanish. Denote the three signed orbit sums, normalized to have coefficient one on their respective representatives, by \(u_1,u_{12},u_4\). Direct boundary counting gives
\[
\partial u_1=[2,3]-[1,3]+[1,2],\quad
\partial u_{12}=4\partial u_1,\quad \partial u_4=0.
\]
Consequently an \(H\)-\(\eta\)-eigenchain \(a u_1+b u_{12}+c u_4\) is a cycle precisely if \(a+4b=0\). Its \([L]\)-coefficient is \(a\), necessarily divisible by \(4\). Thus \(4\mid m\).

Conversely \(z=u_{12}-4u_1\) is an integral \(H\)-\(\eta\)-eigencycle. Its oriented line coefficients vanish at the six lines other than \(L\), while \(\pi(z)=-4[L]\). Since \(T\cong\operatorname{Ind}_H^G\mathbb Z_\eta\) as an integral signed permutation lattice, defining \(s(g[L])=g z\) gives a well-defined integral \(G\)-map with \(\pi s=-4\operatorname{id}_T\). Negating it yields the required \(m=4\). This proves minimality and integral nonsplitting.

## Verification
The standalone `verify_fano.py` reconstructs all \(7\) lines, \(28\) bases, \(168\) automorphisms and the full face actions with integral orientation signs. It checks class counts and all top-homology character values, the surjective relative map using all line-plus-point tetrahedra, the five line-stabilizer orbits with their compatibility tests, the three signed-orbit boundary relations, and the explicit projected cycle realizing exponent four. Run `python3 verify_fano.py`; the stored output is in `verification_output.txt`. No nonstandard numerical library is needed.

## Relationship to prior work
Matroid independence complexes are classically shellable; Klee and Samper explicitly use the Fano matroid as an example, and Ardila–Castillo–Samper establish natural shellings and the wedge description generally. Those results establish the underlying nonequivariant topology and do not constitute new claims here. Moci–Pezzoli's general equivariant comparison between matroid independence homology and lattice-of-flats homology is a stronger *abstract correspondence* applicable to this setting. It does not state this Fano oriented-line integral short exact sequence, determine its exact integral equivariant splitting exponent, or tabulate the present specific characters. Related computations of homology representations for graph complexes associated with Fano incidence structures use different simplicial complexes; a common six-dimensional rational constituent alone is not implication of the present integral extension. The new assertion is the exact integer obstruction together with its concrete equivariant extension and character.

## Limitations
The exact exponent is proved for this canonical seven-point matroid sequence, not for arbitrary matroids or Steiner systems. Rational splitting does not imply an integral \(G\)-module splitting. The representation decomposition is over \(\mathbb C\) (with the two complex-conjugate three-dimensional pieces forming a six-dimensional rational summand); no integral decomposition of \(H_2(K;\mathbb Z)\) is claimed. Exhaustive finite tests support the explicitly finite group/complex computations, while the proof of the extension and exponent is the given integral chain and orbit argument. An equivalent result in unindexed literature is a residual bibliographic risk.

## References
1. Steven Klee and José Alejandro Samper, *Lexicographic shellability, matroids and pure order ideals*, arXiv:1406.1951v1, first posted 2014-06-08; see Sections 2–4, especially Fano examples 3.6 and 4.4. https://arxiv.org/abs/1406.1951
2. Federico Ardila, Federico Castillo, and José Alejandro Samper, *The topology of the external activity complex of a matroid*, arXiv:1410.3870v1, first posted 2014-10-14; Introduction and Theorem 1.3. https://arxiv.org/abs/1410.3870
3. Luca Moci and Gian Marco Pezzoli, *Representations of automorphism groups on the homology of matroids*, arXiv:2001.03760v1, first posted 2020-01-11; Introduction and Theorem 19. https://arxiv.org/abs/2001.03760
4. Standard irreducible character table of \(PSL_2(7)\), e.g. https://en.wikipedia.org/wiki/PSL(2,7) (class sizes and complex irreducibles). The independent finite character enumerator is embedded.
