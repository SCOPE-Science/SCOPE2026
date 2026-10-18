# Geodetic bases of finite projective-plane incidence graphs: flag rigidity and a sharp simultaneous-exchange threshold

## Finding

Let \(\Pi\) be **any** finite projective plane of order \(q\ge 2\), including a non-Desarguesian plane, and let \(G_\Pi\) be its ordinary undirected point–line incidence graph. The geodetic number is
\[
 g(G_\Pi)=2q.
\]
Every minimum geodetic set is uniquely specified by an incident point–line flag \((x,L)\), and is exactly
\[
 S_{x,L}=\bigl(L\setminus\{x\}\bigr)\ \cup\ \bigl(\{M\in\mathcal L:x\in M\}\setminus\{L\}\bigr),
 \qquad x\in L.
\]
The first summand represents \(q\) point-vertices and the second \(q\) line-vertices; the two summands are disjoint vertex types. There are exactly \((q^2+q+1)(q+1)\) minimum geodetic sets, all independent in the incidence graph.

For distinct minimum sets \(S\) and \(T\), define their **replacement distance** to be \(\delta(S,T)=|S\setminus T|=|T\setminus S|\). For an integer \(t\ge1\), join distinct minimum sets in \(\mathcal R_t\) precisely when \(\delta(S,T)\le t\): one may replace up to \(t\) selected vertices simultaneously, and only the endpoint configurations must be geodetic. Then the exact first threshold at which \(\mathcal R_t\) becomes connected is
\[
 t_{\mathrm{conn}}=\min\{q+1,2q-2\}
 =\begin{cases}2,&q=2,\\q+1,&q\ge3.\end{cases}
\]
Indeed every \(\mathcal R_t\) with \(1\le t<t_{\mathrm{conn}}\) is edgeless. In particular, **no single-vertex token jump preserves minimum geodetic status** for any \(q\ge2\).

For each flag there are exactly \(2q\) other bases at distance \(q+1\), exactly \(q^3\) at distance \(2q-2\), and exactly \(2q^2\) at distance \(2q\). When two distance values coincide, the corresponding counts are added.

## Assumptions and scope

A finite projective plane of order \(q\) has \(v=q^2+q+1\) points and equally many lines; each line has \(q+1\) points, each point lies on \(q+1\) lines, and any two distinct points (respectively lines) lie on (respectively intersect in) exactly one line (respectively point). The existence of \(\Pi\) is assumed; no existence claim for a plane of arbitrary order is made.

A geodesic is a shortest path. Its **geodetic interval** \(I(u,w)\) contains every vertex lying on at least one shortest path between \(u\) and \(w\), including endpoints. A set \(S\) is geodetic if \(\bigcup_{u,w\in S}I(u,w)=V(G_\Pi)\). This is ordinary geodetic coverage using the union of **all** shortest paths; it is not the stronger notion that requires assigning one path per endpoint pair. The replacement operation is simultaneous endpoint exchange, not a sequence of potentially infeasible intermediate configurations.

## Proof

**1. Necessary point and line covers.** Write any geodetic set as \(S=A\cup B\), where \(A\) is a set of \(a\) points and \(B\) is a set of \(b\) lines. Every point-vertex that lies on a geodesic between vertices of \(S\) either belongs to \(A\) or lies on some selected line of \(B\). To see this, a shortest path between two points has the form point–line–point; one between two lines has the form line–point–line and its middle point is incident with both selected lines; and a shortest path joining a point to a nonincident line has the form point–line–point–line, with its internal point on the selected endpoint line. The adjacent point–line case has no internal vertices. Dually, every covered line-vertex belongs to \(B\) or passes through a point of \(A\).

A union of \(b\) distinct lines has at most \(1+bq\) points (choose one line, then each further line meets its predecessors and contributes at most \(q\) new points). The bound also holds vacuously at \(b=0\). The dual statement holds for the lines through \(a\) points. Since all \(v\) points and all \(v\) lines are covered,
\[
 v\le a+1+bq,\qquad v\le b+1+aq.
\]
Adding gives \((q+1)(a+b)\ge 2(v-1)=2q(q+1)\), so \(a+b\ge2q\).

**2. Equality classification.** Suppose \(a+b=2q\). Both preceding inequalities must be equalities. Subtracting their equality equations gives \((q-1)(a-b)=0\), hence \(a=b=q\). The \(q\) selected lines cover exactly \(q^2+1\) points, their maximal possible union. Any collection of at least two projective-plane lines attaining the bound \(1+bq\) is concurrent: take their first two lines with intersection \(x\); a further line must meet their union in exactly one point, so it passes through \(x\), and the same induction applies to subsequent lines. Thus \(B\) is the set of the \(q\) lines of the pencil at \(x\) other than a uniquely omitted line \(L\). Their union comprises the entire plane except the \(q\) points of \(L\setminus\{x\}\). All omitted points must belong to \(A\), and since \(|A|=q\), one has \(A=L\setminus\{x\}\). This proves uniqueness of the displayed form.

**3. Existence and exact count.** Conversely, for any incident flag \((x,L)\), the displayed \(S_{x,L}\) is geodetic. Each point on \(L\setminus\{x\}\) is selected. Each other point belongs to a selected line \(M\) through \(x\), and every point of \(M\) lies on a shortest path between any selected point \(p\in L\setminus\{x\}\) and the selected line-vertex \(M\), because \(p\notin M\). Every line \(N\) not passing through \(x\) meets \(L\) in a selected point \(p\), and lies on a shortest path from \(p\) to a selected line through \(x\). All lines through \(x\) other than \(L\) are selected; \(L\) itself lies on the distance-two geodesic joining any two distinct selected points of \(L\), which exist because \(q\ge2\). Hence all vertices are covered. The \(q\) selected points determine \(L\) uniquely and its single omitted point determines \(x\), so distinct flags yield distinct sets. There are \(v(q+1)\) flags. Every selected point lies on \(L\) away from \(x\), whereas every selected line passes through \(x\) and is not \(L\); therefore no selected point is incident with a selected line, proving independence.

**4. Pairwise replacement distances.** Fix flags \((x,L)\ne(y,M)\). If \(x=y\), then \(L\ne M\), the selected point portions are disjoint, and the line portions have \(q-1\) elements in common; hence \(\delta=q+1\). Dually, if \(L=M\), then \(\delta=q+1\).

Suppose \(x\ne y\) and \(L\ne M\). Both cross-incidences \(x\in M\) and \(y\in L\) cannot hold, because then the two distinct lines would both contain \(x,y\). If neither holds, the point portions share the intersection \(L\cap M\), and the line portions share the join \(xy\); thus \(\delta=2q-2\). If exactly one cross-incidence holds, both intersections are empty, so \(\delta=2q\). For a fixed flag, the same-point or same-line cases yield \(2q\) choices. In the noncross case choose \(y\notin L\) in \(q^2\) ways and then a line \(M\ni y\) not through \(x\) in \(q\) ways, giving \(q^3\). The remaining \(2q^2\) flags have a cross-incidence. These categories exhaust every flag.

**5. Sharp connectedness threshold.** The preceding list proves every smaller-than-\(\min\{q+1,2q-2\}\) exchange graph is edgeless. If \(q\ge3\), at the claimed threshold all pairs of flags sharing a point or a line are adjacent. That ordinary flag-adjacency graph is connected: if \(z=L\cap M\), a path from \((x,L)\) to \((y,M)\) goes through \((z,L)\) and \((z,M)\). For \(q=2\), the smaller threshold is two, so adjacency means that neither cross-incidence holds. Any two flags sharing a center, \((x,L),(x,M)\), admit a two-step connection via some \((z,N)\) with \(z\notin L\cup M\) and \(x\notin N\); there are \(q(q-1)>0\) choices for \(z\) and \(q\) choices for \(N\). Any two flags sharing a line, \((x,L),(y,L)\), similarly admit a common opposite neighbor: choose \(z\notin L\), then choose one of the \(q-1\) lines through \(z\) containing neither \(x\) nor \(y\). Thus every edge of the connected ordinary flag-adjacency graph is replaced by a two-step path of opposite flags. The threshold-two graph is connected, completing the proof.

## Verification

The self-contained programs `verify_small_planes.py` and `verify_flags.py` use no external dependencies. Run them with Python 3 from the extracted file directory. The first builds full shortest-path intervals and checks **every** vertex subset of size at most \(2q\) in \(\operatorname{PG}(2,q)\), for \(q=2,3\): it finds respectively \(21\) size-four and \(52\) size-six geodetic bases, and none smaller. It then compares the identified bases and the full pairwise distance histograms against the flag description.

The second independently constructs finite fields of orders \(2,3,4,5\), verifies the projective-plane incidence axioms, computes shortest-path intervals, verifies every flag witness, the distance categories, and the sharp exchange connectivity threshold. Its output for \(q=4\) includes \(105\) flag bases and for \(q=5\) includes \(186\). Recorded outputs are in `small_output.txt` and `flags_output.txt`. Computations are finite consistency checks; the general result for all existing planes, including non-Desarguesian planes, follows from the incidence-axiom proof above.

## Relationship to prior work

Geodetic sets were introduced by Harary, Loukakis and Tsouros (1993). Chartrand, Harary and Zhang (2000; 2002) studied general geodetic sets, extremal bounds and related graph constructions. Douthat and Kong (1996) studied geodetic bases of chordal and split graphs, while Nuenay and Jamil (2015) studied minimal geodetic domination. The present projective-plane incidence graphs have girth six and are neither chordal nor split, and the result concerns plain geodetic coverage rather than additional domination. In particular, general bounds and existence constructions in the cited sources do not identify the flag-form minimum bases of arbitrary projective planes or the sharp simultaneous-exchange threshold.

Related existing research on geodetic sets of complete multipartite graphs and crown graphs addresses different graph families; those descriptions do not imply the present projective-plane result. No priority or absence-of-literature theorem is claimed. Search and source-inspection limits appear in the accompanying review.

## Limitations

The general proof requires the full finite projective-plane axioms and \(q\ge2\), not merely a regular girth-six bipartite graph or an arbitrary symmetric design. The result makes no assertion about orders for which no plane exists. Simultaneous exchanges are endpoint operations and do not require feasibility of intermediate states. The finite exhaustive examples do not establish the infinite-family theorem by themselves. An independent external scientific audit has not been performed.

## References

1. F. Harary, E. Loukakis and C. Tsouros, *The geodetic number of a graph*, Mathematical and Computer Modelling **17** (1993), 89–95, DOI: 10.1016/0895-7177(93)90259-2. The available historical metadata provides the publication month but not a verified original public day.
2. A. L. Douthat and M. C. Kong, *Computing Geodetic Bases of Chordal and Split Graphs*, Journal of Combinatorial Mathematics and Combinatorial Computing **22** (1996), 67–77. Publisher OA PDF: https://combinatorialpress.com/article/jcmcc/Volume%20022/vol-22-paper%207.pdf . Publisher lists publication date 1996-10-31.
3. G. Chartrand, F. Harary and P. Zhang, *Geodetic sets in graphs*, Discussiones Mathematicae Graph Theory **20** (2000), 129–138. DOI: 10.7151/dmgt.1112; bibliographic notice: https://geodesic.mathdoc.fr/item/DMGT_2000_20_1_a9/ .
4. G. Chartrand, F. Harary and P. Zhang, *On the geodetic number of a graph*, Networks **39** (2002), 1–6, DOI: 10.1002/net.10007. Publisher records first online publication on 2001-11-16.
5. H. M. Nuenay and F. P. Jamil, *On Minimal Geodetic Domination in Graphs*, Discussiones Mathematicae Graph Theory **35** (2015), 403–418; https://geodesic.mathdoc.fr/item/DMGT_2015_35_3_a0/ .
