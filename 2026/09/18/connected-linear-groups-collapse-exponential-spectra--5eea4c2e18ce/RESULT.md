# Connected linear groups collapse exponential spectra on classical Banach spaces

## Statement

Let \(A\) be a complex unital Banach algebra. Write \(\operatorname{Inv}(A)\) for its invertible group, \(\operatorname{Inv}_0(A)\) for the connected component of the identity, \(\sigma_A(a)\) for the ordinary spectrum, and
\[
\varepsilon_A(a)=\{\lambda\in\mathbb C:\lambda 1_A-a\notin \operatorname{Inv}_0(A)\}
\]
for the exponential spectrum.

Then the following are equivalent:

1. \(\operatorname{Inv}(A)\) is connected;
2. \(\varepsilon_A(a)=\sigma_A(a)\) for every \(a\in A\).

Consequently, if \(X\) is a complex Banach space whose general linear group \(\operatorname{GL}(X)\) is connected, then
\[
\varepsilon_{\mathcal B(X)}(T)=\sigma_{\mathcal B(X)}(T)
\qquad(T\in\mathcal B(X)).
\]
In particular,
\[
\varepsilon_{\mathcal B(X)}(ST)\setminus\{0\}
=
\varepsilon_{\mathcal B(X)}(TS)\setminus\{0\}
\qquad(S,T\in\mathcal B(X)),
\]
because the ordinary spectrum satisfies Jacobson's identity away from zero.

Classical connectedness results therefore rule out exponential-spectral noncommutativity on each of
\[
c_0,\qquad \ell_p\ (1\le p\le\infty),\qquad C[0,1],\qquad
L_p[0,1]\ (1\le p\le\infty)
\]
over the complex scalars.

The same mechanism applies to every complex hereditarily indecomposable Banach space, and to the more recent contractible-linear-group examples \(L_p(L_q)\) for \(1<p,q<\infty\), \(L_1(L_p)\), \(L_\infty(L_q)\), \(\ell_p(E)\) for \(1<p<\infty\) and reflexive symmetric sequence spaces \(E\), and the corresponding Besov spaces covered by Pliev--Sukochev--Tomskova.

Thus Question 9.2 of Horváth--Kania, which asks whether exponential-spectral commutativity can fail on a classical sequence or function space and which structural properties rule out failure, has a broad negative answer for the standard canonical families above. The question remains open for broader interpretations of "classical" and, in particular, for spaces whose general linear group is disconnected.

## Proof of the collapse criterion

If \(\operatorname{Inv}(A)\) is connected, then
\[
\operatorname{Inv}(A)=\operatorname{Inv}_0(A).
\]
The definitions of ordinary and exponential spectrum therefore give
\[
\varepsilon_A(a)=\sigma_A(a)
\]
for every \(a\in A\).

Conversely, suppose that \(\varepsilon_A(a)=\sigma_A(a)\) for every \(a\in A\). Let \(u\in\operatorname{Inv}(A)\) and set \(a=1_A-u\). Since \(u=1_A-a\) is invertible,
\[
1\notin \sigma_A(a).
\]
By the assumed equality,
\[
1\notin\varepsilon_A(a),
\]
which means exactly that \(u=1_A-a\in\operatorname{Inv}_0(A)\). Hence every invertible belongs to the identity component, so \(\operatorname{Inv}(A)\) is connected.

For \(A=\mathcal B(X)\), the invertible group is \(\operatorname{GL}(X)\), giving the operator-space assertion. The usual Jacobson relation
\[
\sigma(ST)\setminus\{0\}=\sigma(TS)\setminus\{0\}
\]
then gives exponential-spectral commutativity away from zero.

## Classical spaces covered

The implication "connected invertible group \(\Rightarrow\) exponential spectrum equals ordinary spectrum" is not new; it was already explicitly noted in the 2009 MathOverflow discussion that preceded the Klaja--Ransford counterexample. The point here is its combination with the classical homotopy theory of general linear groups in direct response to the new 2026 operator-algebra question.

De Rancourt's survey of connected-component results records that, over both real and complex scalars, the general linear groups of \(c_0\), \(\ell_p\) for \(1\le p<\infty\), \(C[0,1]\), \(L_1[0,1]\), \(L_\infty[0,1]\), and \(\ell_\infty\) are connected, and that \(\operatorname{GL}(L_p[0,1])\) is connected for \(1<p<\infty\). Mityagin's 1970 survey independently records the contractibility results for \(\operatorname{GL}(\ell_p)\), \(1\le p<\infty\), and \(\operatorname{GL}(c_0)\), as well as Kuiper's Hilbert-space theorem.

De Rancourt also proves that \(\operatorname{GL}(X)\) is connected for every complex hereditarily indecomposable Banach space \(X\). More recently, Pliev--Sukochev--Tomskova proved contractibility of the general linear groups of several Lebesgue--Bochner, vector-valued sequence, and Besov spaces. Every one of these connectedness or contractibility theorems therefore yields pointwise collapse of exponential spectrum to ordinary spectrum.

## Sharp boundary and comparison with stable rank

Connectedness of \(\operatorname{GL}(X)\) is an exact criterion for the stronger statement
\[
\varepsilon(T)=\sigma(T)\quad\text{for every }T\in\mathcal B(X),
\]
but it is not necessary for exponential-spectral commutativity alone.

Indeed, Daniel and Ghosh proved that exponential spectrum is commutative in
\(\mathcal B(\ell_p\oplus\ell_q)\) in the range treated in their paper, whereas classical work of Douady, summarized by de Rancourt, shows that the general linear group of a direct sum of two distinct spaces among the \(\ell_p\)'s and \(c_0\) is disconnected. Thus there are at least two genuinely different no-twisting mechanisms: complete component collapse, and weaker Jacobson-pair invariance across nontrivial components.

There is also a useful separation from stable rank. Horváth--Kania note that
\[
\operatorname{tsr}\mathcal B(H)=\infty
\]
for infinite-dimensional Hilbert space \(H\). Nevertheless \(\operatorname{GL}(H)\) is contractible, so
\[
\varepsilon_{\mathcal B(H)}(T)=\sigma_{\mathcal B(H)}(T)
\]
for every \(T\). Hence infinite topological stable rank by itself is not evidence that exponential-spectral twisting can occur.

## Relation to the 2026 open problem

Horváth and Kania construct the first bounded-operator example in which exponential spectra of \(ST\) and \(TS\) differ away from zero. Their Question 9.2 asks whether such failure can occur for a classical sequence or function space, and more generally which structural properties of \(X\) exclude it.

The connectedness criterion gives a direct structural answer and eliminates the standard canonical spaces \(c_0\), all \(\ell_p\), \(C[0,1]\), and all \(L_p[0,1]\). It also eliminates several newer function-space classes whose linear groups are known to be contractible. This does not settle Question 9.2 in full, because "classical sequence or function space" is not a formally delimited class and disconnected general linear groups can still support exponential-spectral commutativity.

## Limitations and originality status

The algebraic equivalence proved above is elementary, and its forward implication was publicly observed long before the 2026 question. No novelty is claimed for that implication or for the classical connectedness theorems themselves.

The originality claim is narrower: to the best of our knowledge, the searched literature does not record the systematic application of those connectedness results to Horváth--Kania Question 9.2, including the simultaneous exclusion of the standard \(c_0\), \(\ell_p\), \(C[0,1]\), and \(L_p[0,1]\) families, the modern Lebesgue--Bochner/Besov examples, and the contrast with infinite stable rank. Searches using the paper title, arXiv identifier, "exponential spectrum", "general linear group", "connected", "contractible", the named classical spaces, and Mityagin/Pliev terminology found no such treatment.

The Daniel--Ghosh full text was not inspected here; only its published abstract and the precise theorem-level summary in Horváth--Kania were used for the disconnected-group comparison. The Pliev--Sukochev--Tomskova extension is based on the published bibliographic record and an author seminar abstract describing the contractibility theorems. The core conclusion for the standard classical spaces rests on the explicit connectedness summary in de Rancourt and the elementary collapse argument above.

## References

1. B. Horváth and T. Kania, *Twisting exponential spectra*, arXiv:2609.05362v1 (2026). https://arxiv.org/abs/2609.05362
2. N. de Rancourt, *Connected components of the general linear group of a real hereditarily indecomposable Banach space*, arXiv:2009.04687; Studia Mathematica. https://arxiv.org/abs/2009.04687
3. B. S. Mityagin, *The homotopy structure of the linear group of a Banach space*, Russian Math. Surveys 25:5 (1970), 59--103. https://doi.org/10.1070/RM1970v025n05ABEH003814
4. M. Pliev, F. Sukochev and A. Tomskova, *The homotopy type of the linear group of Lebesgue--Bochner and Besov spaces*, J. Funct. Anal. 289 (2025), 111178. https://doi.org/10.1016/j.jfa.2025.111178
5. S. Daniel and A. Ghosh, *A note on commutativity of the exponential spectrum in the operator algebra \(\mathcal B(\ell^p\oplus\ell^q)\)*, Acta Math. Hungar. 177 (2025), 280--296. https://doi.org/10.1007/s10474-025-01571-x
6. M. Younsi, *In a Banach algebra, do ab and ba have almost the same exponential spectrum?*, MathOverflow (2009; later updated). https://mathoverflow.net/questions/2369/
