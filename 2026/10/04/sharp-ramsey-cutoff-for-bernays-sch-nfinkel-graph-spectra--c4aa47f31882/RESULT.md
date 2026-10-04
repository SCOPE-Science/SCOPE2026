# Sharp Ramsey cutoff for Bernays–Schönfinkel graph spectra
## Finding
Fix integers \(k\ge 0\) and \(\ell\ge 2\). Let \(R(\ell,\ell)\) be the least integer \(R\) such that every simple graph on \(R\) vertices contains either a clique or an independent set of size \(\ell\). Consider a finite simple-graph sentence
\[
\Phi=\exists x_1\cdots\exists x_k\,orall y_1\cdotsorall y_\ell\,\psi,
\]
where \(\psi\) is quantifier-free. Put
\[
N(k,\ell)=k+igl(R(\ell,\ell)-1igr)2^k.
\]
If \(\Phi\) has a model with more than \(N(k,\ell)\) vertices, then it has a model of every order \(n\ge k+\ell\). Hence, if the spectrum of \(\Phi\) is finite, its largest element is at most \(N(k,\ell)\). The bound is sharp for every \(k\) and \(\ell\): there is a sentence with this prefix whose spectrum is finite and whose largest model has exactly \(N(k,\ell)\) vertices.

For \(\ell=2\), since \(R(2,2)=2\), the endpoint is \(k+2^k\). For \(\ell=3\), since \(R(3,3)=6\), the endpoint is \(k+5\cdot 2^k\).

## Assumptions and scope
Graphs are finite, nonempty, simple, undirected, and use adjacency and equality only. The statement concerns sentences in prenex Bernays–Schönfinkel form with exactly \(k\) existential quantifiers followed by exactly \(\ell\) universal quantifiers; some quantified variables may be semantically redundant. The result gives the optimal universal upper endpoint for finite spectra at fixed \(k,\ell\). It does not classify which subsets below the endpoint occur as spectra.

## Proof
Assume \(G\models\Phi\), witnessed by vertices \(x_1,\ldots,x_k\), and let \(U\) be the set of distinct witnesses, so \(|U|\le k\). Each vertex of \(G-U\) has one of at most \(2^k\) adjacency profiles to the ordered witness tuple. If
\[
|G|>k+igl(R(\ell,\ell)-1igr)2^k,
\]
then \(|G-U|>(R(\ell,\ell)-1)2^k\). By the pigeonhole principle, some profile class contains at least \(R(\ell,\ell)\) vertices. By the definition of the diagonal Ramsey number it contains a set \(X\) of \(\ell\) vertices inducing either a clique or an independent set.

Because \(\Phi\) is universal after the witnesses are fixed, the induced subgraph \(H=G[U\cup X]\), with the same witness assignment, still satisfies \(\Phi\). All vertices of \(X\) have the same adjacency to every witness, while every pair of distinct vertices of \(X\) has the same adjacency value. Replace \(X\) by an arbitrarily large set \(X'\) with the same witness profile and with all distinct pairs adjacent if \(X\) was a clique, and nonadjacent if \(X\) was independent. Any assignment to the \(\ell\) universal variables in the enlarged graph uses at most \(\ell\) distinct vertices of \(X'\); map those distinct vertices injectively into \(X\), fixing all witnesses. Equality, adjacency among cloned vertices, and adjacency from cloned vertices to witnesses are preserved, so every atomic formula and hence \(\psi\) has the same truth value. Therefore every enlargement obtained this way is again a model. Since one may choose \(|X'|\) freely, models exist for every order at least \(k+\ell\) after adding enough clones; if \(|U|<k\), simply choose \(|X'|\) large enough to reach the requested total order.

For sharpness, fix a Ramsey-critical graph \(Q_\ell\) on \(R(\ell,\ell)-1\) vertices with no clique and no independent set of size \(\ell\); such a graph exists by minimality of \(R(\ell,\ell)\). Use \(k\) existential witnesses and require them to be distinct. For every \(\ell\)-tuple of distinct nonwitness vertices having one common adjacency profile to the witnesses, require that its induced graph is neither complete nor empty. This condition is quantifier-free once the existential witnesses and universal tuple are named. Ramsey's theorem then forces each of the \(2^k\) profile classes to have size at most \(R(\ell,\ell)-1\), so every model has at most \(N(k,\ell)\) vertices. Equality is attained by taking, for each of the \(2^k\) witness profiles, a disjoint copy of \(Q_\ell\), assigning that profile to its vertices, and choosing arbitrary edges between different profile classes. Thus the bound is exact.

## Verification
The proof is symbolic and uses only the defining property of \(R(\ell,\ell)\). A supplementary checker exhaustively verified \(R(3,3)=6\) over all \(2^15=32768\) labelled graphs on six vertices and verified that the five-cycle is a critical five-vertex witness. It returned `VERIFY_OK R33=6 exhaustive_32768 C5_critical`. This computation checks the concrete \(\ell=3\) specialization, not the general proof.

## Relationship to prior work
Ramsey's theorem for Bernays–Schönfinkel graph sentences is recorded in Pikhurko and Verbitsky's survey: for a sentence with \(k\) existential and \(\ell\) universal variables, they state the coarser threshold \(2^k4^\ell\), and their proof already selects \(R(\ell,\ell)\) same-profile vertices before using the estimate \(R(\ell,\ell)<4^\ell\). Thus the improved upper bound is latent in that proof. The additional point here is the exact optimal endpoint and its matching construction from a Ramsey-critical graph. Targeted searches did not locate a published statement of this sharp fixed-\((k,\ell)\) endpoint.

## Limitations
The result does not compute \(R(\ell,\ell)\); exact numerical endpoints are therefore explicit only when the corresponding Ramsey number is known. It also does not characterize all possible finite spectra below the endpoint. Priority risk remains because the sharpness construction is elementary once the Ramsey proof is written with the exact Ramsey number, so it may exist as folklore or an unindexed exercise.

## References
1. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865 (first posted 2010-03-25); Contemporary Mathematics 558 (2011), 129–180, DOI:10.1090/conm/558/11050. See the Bernays–Schönfinkel spectrum theorem and its Ramsey-number proof in Section 7.3.
2. F. P. Ramsey, *On a problem of formal logic*, Proceedings of the London Mathematical Society, Series 2, 30 (1930), 264–286.
