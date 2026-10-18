# Complete lean-colouring classification of finite projective planes

## Finding

**Theorem.** Let \(\Pi\) be any finite projective plane of order \(q\ge 2\), and let \(H_\Pi\) be the hypergraph whose vertices are the points of \(\Pi\) and whose hyperedges are its lines. A *lean colouring* is a point-colouring with at least two colours such that every line is either monochromatic or rainbow (all its points have different colours). Every lean colouring is of exactly one of the following two kinds:

1. All \(q^2+q+1\) points have pairwise distinct colours.
2. Exactly one line is monochromatic, its \(q+1\) points share one colour, and the remaining \(q^2\) points have pairwise distinct colours different from the line colour.

Both kinds occur. Consequently,
\[
\operatorname{Lean}(H_\Pi)=q^2+1,
\]
and the feasible numbers of used colours form precisely \(\{q^2+1,\,q^2+q+1\}\). Hence the lean chromatic spectrum has \(q-1\) consecutive omitted integers.

For every integer palette size \(t\ge0\), the exact number \(L_\Pi(t)\) of lean colourings into \(t\) *named, available* colours (not necessarily all used) is
\[
L_\Pi(t)=(t)_{q^2+q+1}+(q^2+q+1)t(t-1)_{q^2},
\]
where \((t)_r=t(t-1)\cdots(t-r+1)\), with \((t)_0=1\), and for nonnegative integral \(t<r\), \((t)_r=0\). There are exactly \((q^2+q+1)(q^2+1)!\) optimal colourings when their \(q^2+1\) colours are named, and exactly \(q^2+q+1\) optimal colour partitions up to renaming colours.

The largest incidence degree of a vertex of \(H_\Pi\) is \(q+1\). Thus \(\operatorname{Lean}(H_\Pi)=q^2+1>q+2\) for every \(q\ge2\). In particular these examples disprove the incidence-degree inequality \(\operatorname{Lean}(H)\le\Delta(H)+1\) stated in Corollary 4.3.1 of reference [1], where \(\Delta(H)\) counts hyperedges incident to a hypergraph vertex. Prime-order planes yield an infinite, unbounded-ratio family of counterexamples.

## Assumptions and scope

A finite projective plane of order \(q\) is an incidence structure in which every line contains \(q+1\) points, every point lies on \(q+1\) lines, any two points determine exactly one line, and any two lines intersect in exactly one point. These axioms imply \(q^2+q+1\) points and equally many lines. No coordinatization, transitivity assumption, or Desarguesian hypothesis is used. Statements apply to every finite plane of order \(q\ge2\) that exists, including non-Desarguesian planes.

The colour rule is precisely that of [1]: the colouring must be globally nonconstant, and on each hyperedge either all colours agree or all colours are distinct. A rainbow line is not a line with merely two colours. Falling-factorial counts include colourings that omit some colours of the available palette.

## Proof

Write \(n=q^2+q+1\). Let \(c\) be any lean colouring. Call a line *mono* when all of its points receive one colour.

**Step 1: at most one mono line.** Suppose distinct lines \(L_1,L_2\) are mono. Because they meet, they have the same monochromatic colour, say \(a\). Take any point \(P\) outside \(L_1\cup L_2\). Choose \(X\in L_1\setminus L_2\). The line \(PX\) meets \(L_2\) in a point \(Y\). As \(PX\ne L_1\), this \(Y\) is different from the intersection \(L_1\cap L_2\), and \(X\ne Y\). Both \(X,Y\) have colour \(a\), so \(PX\) cannot be rainbow. It must be mono, forcing \(c(P)=a\). Every point in \(L_1\cup L_2\) also has colour \(a\). This makes \(c\) globally constant, contradicting its definition. Thus two distinct mono lines cannot occur in a lean colouring.

**Step 2: absence of mono lines.** When no line is mono, every line is rainbow. Any two distinct points lie on one line; therefore all points have different colours. This is the first kind in the theorem.

**Step 3: exactly one mono line.** Let \(L\) be mono with colour \(a\). No point \(P\notin L\) can have colour \(a\): if such a point existed, then for any other point \(Q\notin L\) distinct from \(P\), the line \(PQ\) would meet \(L\) at some point \(R\) of colour \(a\). Since \(P,R\) have the same colour, \(PQ\) must be mono and \(Q\) would also have colour \(a\), making the entire colouring constant. (When \(Q=P\), its colour is already \(a\).) Thus all outside points have colours different from \(a\).

If two distinct outside points \(P,Q\) shared colour \(b\), the line \(PQ\) would meet \(L\) at a point of colour \(a\ne b\). It would be neither rainbow nor mono, a contradiction. Hence all outside points receive pairwise different colours. Conversely, choose any line \(L\), give all its points one colour, and give all \(q^2\) outside points mutually distinct colours different from it. Any line other than \(L\) meets \(L\) in one point and has \(q\) outside points, so it is rainbow. This is a valid lean colouring. The all-distinct colouring is also valid.

**Step 4: spectrum, enumeration, and degree comparison.** The first kind uses \(n\) colours and the second uses exactly \(q^2+1\); no other kinds exist. For a palette of \(t\) named colours, the first kind has \((t)_n\) choices. For the second kind choose one of the \(n\) mono lines, its colour in \(t\) ways, then inject the \(q^2\) outside points into the remaining \(t-1\) colours in \((t-1)_{q^2}\) ways. The mono line is unique, so these classes are disjoint and no colouring is counted twice. Substituting \(t=q^2+1\) gives the optimal-colouring count, while modulo colour renaming there is one optimal partition for each mono line. The number of omitted integers strictly between the two feasible colour counts is \(n-(q^2+1)-1=q-1\).

Finally, each point lies on exactly \(q+1\) lines, so the incidence degree equals \(q+1\). For every integer \(q\ge2\), \(q^2+1>q+2\). For every prime \(q\), a projective plane over \(\mathbb F_q\) exists, yielding infinitely many examples with \((q^2+1)/(q+2)\) unbounded. This completes the proof.

## Verification

The accompanying standalone program `verify_projective_lean.py` enumerates the incidence structures of \(\operatorname{PG}(2,p)\) over the prime fields of orders \(p=2,3,5,7\) and checks the projective plane axioms, the claimed line-monochromatic constructive colourings, and the first-order degree comparison. For \(p=2\), it additionally exhausts all \(877\) set partitions of seven labeled points (one representative per possible colour-renaming class), verifies the lean rule line by line, and finds exactly seven lean partitions using five colours and one using seven. It finds no valid partition using two, three, four, or six colours. The program checks actual assignments, not merely the displayed formula.

Run `python verify_projective_lean.py` using Python 3.8 or newer. This finite verification corroborates the proof but does not establish the theorem for unbounded orders; Steps 1–4 provide the unrestricted proof.

## Relationship to prior work

Reference [1] introduced the lean number and its equivalent incidence-graph and simplicial-complex formulations. Its connected-uniform lower bound gives only \(q+1\) for these \((q+1)\)-uniform hypergraphs. Its wide-path result is inapplicable because distinct lines meet in exactly one point, never two; its \(r\)-complete result is inapplicable because noncollinear triples are not contained in any line. Its valid two-section bound gives only \(\operatorname{Lean}(H_\Pi)\le\chi(K_n)=n\). Corollary 4.3.1 of [1] instead asserts an incidence-vertex-degree upper bound of \(\Delta(H)+1\), and its proof identifies this degree with the two-section degree. Here these degrees are \(q+1\) and \(q^2+q\), respectively, and the asserted incidence-degree inequality is false.

Reference [2] studies *rainbow-free* point colourings of finite projective planes, with balanced colour classes. Its admissible configurations require every line to have a repeated colour, whereas a lean colouring requires each line either to be entirely one colour or to have no repetition at all. Neither its objective nor its colour admissibility condition gives the present classification.

## Limitations

This statement concerns only line hypergraphs of finite projective planes and does not classify all linear uniform hypergraphs or higher-dimensional incidence structures. Existence of a projective plane is not assumed for orders where existence is unknown. The published incidence-degree claim is contradicted as written, not every potentially intended variant involving degrees of two-section graphs. No independent mathematical audit has been performed; an equivalent prior observation under a different terminology is a residual bibliographic risk.

## References

[1] Harrison J. Piehowski, *The Lean Number of a Hypergraph*, arXiv:2607.14015, first publicly posted July 15, 2026. Sections 1, 3, 4; especially Lemma 4.1, Lemma 4.4, and Corollary 4.3.1. https://arxiv.org/abs/2607.14015

[2] Zoltán L. Blázsik, Aart Blokhuis, Štefko Miklavič, Zoltán Lóránt Nagy, and Tamás Szőnyi, *On the balanced upper chromatic number of finite projective planes*, preprint dated November 24, 2020; *Discrete Mathematics*, 2021. https://real.mtak.hu/134900/1/Balanced_upper_chromatic_number_of_PG_2_q_revision.pdf
