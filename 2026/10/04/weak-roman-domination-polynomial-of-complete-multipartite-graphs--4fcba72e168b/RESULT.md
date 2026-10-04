# Weak Roman domination polynomial of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph, with \(r\ge2\) and parts \(V_1,\ldots,V_r\). A weak Roman dominating function is a map \(f:V(G)\to\{0,1,2\}\) such that, for every vertex \(v\) with \(f(v)=0\), one can choose a neighbor \(u\) with \(f(u)>0\), move one unit from \(u\) to \(v\), and obtain a positive-support set that dominates \(G\).

For each part put
\[
w_i=\sum_{v\in V_i}f(v),\qquad z_i=|\{v\in V_i:f(v)=0\}|,
\]
and let \(J=\{i:w_i>0\}\). Then \(f\) is weak Roman dominating exactly when one of the following mutually exhaustive alternatives holds.

1. \(|J|\ge3\).
2. \(J=\{i,j\}\), and
\[
(w_j\ge2\text{ or }z_i\le1)\quad\text{and}\quad(w_i\ge2\text{ or }z_j\le1).
\]
3. \(J=\{i\}\), every vertex of \(V_i\) is positive, and either \(n_i\ge2\), or \(n_i=1\) with the unique value equal to \(2\), or every part of \(G\) is a singleton.

This classification gives the entire weight enumerator
\[
W_G(x)=\sum_f x^{\sum_{v\in V(G)}f(v)},
\]
where the sum ranges over all weak Roman dominating functions. Define
\[
A_i=(1+x+x^2)^{n_i}-1,\qquad F_i=(x+x^2)^{n_i},\qquad E_i=n_i x,
\]
\[
D_i=\sum_{z=2}^{n_i-1}\binom{n_i}{z}(x+x^2)^{n_i-z},
\]
and let \(E_i^{\star}=E_i\) when \(n_i\ge3\), and \(E_i^{\star}=0\) otherwise. If \(s\) is the number of singleton parts and \(N=\sum_i n_i\), put
\[
Q_{\ge3}(x)=(1+x+x^2)^N-1-\sum_iA_i-\sum_{i<j}A_iA_j,
\]
and
\[
Q_1(x)=\begin{cases}
\sum_iF_i,& n_1=\cdots=n_r=1,\\
\sum_iF_i-sx,&\text{otherwise.}
\end{cases}
\]
Then
\[
W_G(x)=Q_1(x)+\sum_{i<j}\left(A_iA_j-D_iE_j-E_iD_j+E_i^{\star}E_j^{\star}\right)+Q_{\ge3}(x).
\]

As a scalar corollary, the least exponent of \(W_G(x)\) is \(1\) when every part is a singleton, and otherwise
\[
\gamma_r(G)=\min\left\{4,\max\left\{2,\min_i n_i\right\}\right\}.
\]
The scalar minimum for complete multipartite graphs is treated as prior territory; the finding here is the all-function structural classification and the resulting exact enumerator.

## Assumptions and scope
Graphs are finite, simple, and connected. Thus \(r\ge2\) and every \(n_i\ge1\). The weak Roman rule is the original one-move rule: after moving one unit from the chosen positive neighbor to the attacked zero vertex, the new positive support must dominate the graph. No claim is made for finite-order variants requiring several successive moves, foolproof variants requiring every legal neighboring guard to work, or total weak Roman domination.

The polynomial records weight, not support size. Distinct vertex labelings are counted separately even when they have the same partwise profile.

## Proof
First note the elementary support criterion for complete multipartite graphs. A nonempty set \(D\subseteq V(G)\) dominates \(G\) if and only if either \(D\) meets at least two parts, or \(D=V_i\) for one part \(V_i\). Indeed, two met parts dominate every vertex by a vertex in the opposite part; if \(D\) lies in one part, an omitted vertex of that same part has no neighbor in \(D\).

Suppose first that \(|J|\ge3\). Let \(v\) be any zero vertex. It has a positive neighbor in every supported part other than its own. Move one unit from any such neighbor \(u\). If the support of \(u\)'s part disappears, at least two originally supported parts remain, except that when \(v\) lies in a previously unsupported part the new part replaces the disappearing one. Thus the post-move support still meets at least two parts and dominates. Hence every labeling with at least three supported parts is weak Roman dominating.

Now let \(J=\{i,j\}\). A zero vertex outside \(V_i\cup V_j\) is always protectable: moving from either supported part leaves positive support in two parts, either the two old parts or one old part together with the attacked vertex's part. Consider instead a zero vertex \(v\in V_i\). Its defender must lie in \(V_j\). If \(w_j\ge2\), one unit can be moved while leaving a positive vertex in \(V_j\): either the defender had value \(2\), or a second positive vertex remains. The post-move support therefore still meets both \(V_i\) and \(V_j\). If \(w_j=1\), the unique positive vertex of \(V_j\) has value \(1\) and disappears after the move. The new support lies entirely in \(V_i\), so by the support criterion it dominates exactly when the attacked vertex was the only zero vertex of \(V_i\), namely \(z_i\le1\). This proves the first condition; the second follows symmetrically.

Finally suppose \(J=\{i\}\). Any zero vertex inside \(V_i\) has no positive neighbor, so necessarily every vertex of \(V_i\) is positive. If \(n_i\ge2\), moving one unit from a vertex of \(V_i\) to any attacked vertex outside leaves another positive vertex in \(V_i\), hence gives support in two parts. If \(n_i=1\) and its value is \(2\), one unit remains at that vertex and the same conclusion holds. If \(n_i=1\) and its value is \(1\), the move leaves only the attacked vertex positive; this dominates exactly when the attacked vertex is the whole of its part. Since every outside zero vertex must be defendable, every part must then be a singleton. This proves the classification.

For enumeration, \(A_i\) counts labelings on \(V_i\) with positive support, \(F_i\) counts labelings with every vertex positive, \(E_i\) counts the weight-one labelings, and \(D_i\) counts positive-support labelings with at least two zeros. Thus for a fixed pair \(i<j\), all two-support labelings contribute \(A_iA_j\). The first forbidden condition contributes \(D_iE_j\), the symmetric condition contributes \(E_iD_j\), and their intersection occurs exactly when both parts have size at least three and both carry a single label \(1\), giving \(E_i^{\star}E_j^{\star}\). Inclusion-exclusion gives the displayed pair term. The term \(Q_{\ge3}\) is simply the generating function for labelings supported on at least three parts. The one-support term is \(\sum_iF_i\), except that a singleton part carrying the sole label \(1\) is invalid unless all parts are singleton; this gives the correction \(-sx\).

The least exponent follows directly. A complete graph admits a single unit. Otherwise a singleton part supports a valid value \(2\) labeling of weight \(2\); a part of size \(2\) can be fully occupied with two units; a smallest part of size \(3\) gives weight \(3\); and when every part has size at least \(4\), no weight below \(4\) satisfies the two-support conditions, while one label \(2\) in each of two parts gives weight \(4\).

## Verification
The accompanying verifier independently implements the weak Roman move rule from the definition and the structural criterion above. It exhausts every ordered complete-multipartite part profile of total order at most \(8\), checks every \(3^N\) vertex labeling, compares rule membership with the theorem, and separately compares the coefficient vector obtained by brute force with the displayed polynomial formula. The packaged replay returned `VERIFY_OK graph_profiles=247 labelings=997929 coefficient_checks=3761 max_order=8`. The finite census is a stress test only; the proof above establishes the theorem for arbitrary positive part sizes.

## Relationship to prior work
Henning and Hedetniemi introduced weak Roman domination as a one-move guard-transfer relaxation of Roman domination. The accessible bibliographic record gives an exact public date of 6 May 2003 for that paper. Burger, Cockayne, Gründlingh, Mynhardt, van Vuuren, and Winterbach later placed weak Roman domination inside a finite-order guard framework. Their full text explicitly says that the previously studied domination parameters had already been determined for complete multipartite graphs, so the minimum weak Roman number for this family is not claimed here as original. Their Section 4.3 then gives exact values for generalized finite-order parameters on complete bipartite graphs, again at the scalar minimum level.

Targeted searches using the aliases “weak Roman dominating function,” “smart weak Roman domination,” “guard function,” “complete multipartite,” “complete bipartite,” “weight enumerator,” and “generating polynomial” located scalar, extremal, algorithmic, and variant results, but no inspected source that classifies every weak Roman dominating labeling of an arbitrary complete multipartite graph or gives the weight enumerator above. The closest modern general papers compare weak Roman domination to other domination parameters rather than enumerate all feasible functions.

## Limitations
The theorem does not address repeated attacks, foolproof protection, total weak Roman domination, or other Roman-type variants. The verifier is exhaustive only through order \(8\). The 2003 foundational full text was not available from the inspected public record during this run, so its abstract and bibliographic metadata were used for the definition and date, while the 2004 finite-order paper was inspected in full at the relevant definition and complete-bipartite sections. There remains a residual bibliographic risk that an older enumerative result is indexed under guard-allocation terminology rather than the standard weak Roman name.

## References
1. M. A. Henning and S. T. Hedetniemi, “Defending the Roman Empire—A new strategy,” Discrete Mathematics 266 (2003), 239–251, DOI 10.1016/S0012-365X(02)00811-7.
2. A. P. Burger, E. J. Cockayne, W. R. Gründlingh, C. M. Mynhardt, J. H. van Vuuren, and W. Winterbach, “Finite Order Domination in Graphs,” Journal of Combinatorial Mathematics and Combinatorial Computing 49 (2004), 159–175.
3. P. Roushini Leely Pushpam and T. N. M. Malini Mai, “Weak roman domination in graphs,” Discussiones Mathematicae Graph Theory 31 (2011), 161–170, DOI 10.7151/dmgt.1532.
4. M. Chellali, T. W. Haynes, and S. T. Hedetniemi, “Bounds on weak roman and 2-rainbow domination numbers,” Discrete Applied Mathematics 178 (2014), 27–32, DOI 10.1016/j.dam.2014.06.016.
