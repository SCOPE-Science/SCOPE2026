# Totally disconnected nondegenerate fibers force Cantor orbit sets

## Finding
Let \(X\) be a compact metric space and let \(F:X\to 2^X\) be upper semicontinuous, where \(2^X\) is the family of nonempty compact subsets of \(X\). For \(z\in X\), write
\[
\mathcal O_F(z)=\{(x_n)_{n\ge1}\in X^{\mathbb N}:x_1=z,\ x_{n+1}\in F(x_n)\text{ for every }n\ge1\}.
\]
If every fiber \(F(x)\) is nondegenerate and totally disconnected, then \(\mathcal O_F(z)\) is homeomorphic to the Cantor set for every \(z\in X\).

Two independent structural statements explain the result. If every fiber is totally disconnected, then every \(\mathcal O_F(z)\) is totally disconnected. If every fiber is nondegenerate, then every \(\mathcal O_F(z)\) has no isolated points. Upper semicontinuity makes \(\mathcal O_F(z)\) closed in the compact metrizable product \(X^{\mathbb N}\). Thus the three hypotheses separately provide total disconnectedness, absence of isolated points, and compactness.

This answers Question 3.18 of Amorocho--Camargo--Macías affirmatively and extends their Theorem 3.16 from finite nondegenerate fibers to arbitrary nondegenerate totally disconnected fibers.

## Assumptions and scope
The values of \(F\) are nonempty compact subsets of \(X\), as in the standard notation \(2^X\) used by the source. No connectedness assumption on \(X\) is needed for the argument. The conclusion uses the classical characterization that every nonempty compact metrizable space with no isolated points and with all connected subsets singletons is homeomorphic to the standard Cantor set.

The total-disconnectedness argument itself does not require upper semicontinuity. Likewise, the no-isolated-points argument uses only nonempty nondegenerate fibers and the product topology. Upper semicontinuity enters only to guarantee that the orbit set is closed, hence compact.

## Proof
Fix \(z\in X\).

First suppose every fiber \(F(x)\) is totally disconnected. Let \(C\subseteq\mathcal O_F(z)\) be connected. The first coordinate projection is constant on the whole orbit set, so \(\pi_1(C)=\{z\}\). Assume inductively that \(\pi_n(C)=\{a_n\}\). For every orbit in \(C\), its next coordinate belongs to \(F(a_n)\), hence
\[
\pi_{n+1}(C)\subseteq F(a_n).
\]
Because \(\pi_{n+1}\) is continuous and \(C\) is connected, \(\pi_{n+1}(C)\) is connected. Since \(F(a_n)\) is totally disconnected, \(\pi_{n+1}(C)\) is a singleton. By induction, every coordinate projection of \(C\) is a singleton. Two elements of a product agreeing in every coordinate are equal, so \(C\) itself is a singleton. Therefore \(\mathcal O_F(z)\) is totally disconnected.

Now suppose every fiber is nondegenerate. Let \(x=(x_n)_{n\ge1}\in\mathcal O_F(z)\) and let \(U\) be any neighborhood of \(x\) in the product topology. There is an integer \(N\) such that every orbit agreeing with \(x\) through coordinate \(N\) lies in a sufficiently small basic neighborhood contained in \(U\); equivalently one can use the usual summable product metric and take \(N\) so that the tail diameter is smaller than the prescribed radius. Since \(F(x_N)\) is nondegenerate, choose
\[
y\in F(x_N)\setminus\{x_{N+1}\}.
\]
Set the first \(N\) coordinates equal to those of \(x\), set the next coordinate equal to \(y\), and then recursively choose each later coordinate from the nonempty value of \(F\) at the preceding coordinate. The resulting sequence is an orbit in \(\mathcal O_F(z)\), belongs to \(U\), and differs from \(x\). Hence \(x\) is not isolated. Since \(x\) was arbitrary, \(\mathcal O_F(z)\) has no isolated points.

Finally, upper semicontinuity of a compact-valued map on a compact metric space implies the graph of \(F\) is closed. Equivalently, as proved in Theorem 3.11 of the source, \(\mathcal O_F(z)\) is closed in \(X^{\mathbb N}\). The product is compact and metrizable, so \(\mathcal O_F(z)\) is compact and metrizable. It is nonempty because the values of \(F\) are nonempty and an orbit can be chosen recursively. Combining compactness, total disconnectedness, and absence of isolated points gives that \(\mathcal O_F(z)\) is a Cantor set.

## Verification
The proof was reconstructed directly from the definitions. The coordinate-projection induction checks total disconnectedness without assuming that iterated images \(F^n(z)\) are totally disconnected. This avoids a possible false shortcut: a union of totally disconnected fibers need not itself be totally disconnected.

For the no-isolated-points part, the source's proof of Theorem 3.16 was inspected. Its tail-perturbation argument uses nondegeneracy but not finiteness of the fibers. The only place finiteness is used there is the final total-disconnectedness step, where the source observes that every coordinate projection is finite. Replacing that last step by the connected-projection induction above removes finiteness exactly.

Boundary cases were also checked. If some fiber is a singleton, the no-isolated-points conclusion can fail, as the source's examples show. If upper semicontinuity is removed, the orbit set need not be closed, so the Cantor conclusion can fail even if the two internal topological properties persist.

## Relationship to prior work
Amorocho, Camargo, and Macías define forward orbit sets for upper semicontinuous maps and prove that each fixed-base orbit set is closed. Their Theorem 3.16 proves the Cantor conclusion when every fiber is finite and nondegenerate. Immediately afterward they ask in Question 3.18 whether the same conclusion follows when every fiber is merely nondegenerate and totally disconnected. The argument above answers that question affirmatively.

There is substantial literature on Cantor generalized inverse limits of set-valued maps. Alvin--Greenwood--Kelly characterize Cantor generalized inverse limits through the domain set \(\mathrm D(F)\), and Capulín--Ruiz del Portal--Sánchez-Garrido obtain Cantor inverse limits under hypotheses involving \(\operatorname{Dom}(F)\) and unions of mappings. Those results concern the inverse-limit relation \(x_n\in F(x_{n+1})\) and different global hypotheses. The present claim concerns the fixed-initial-point forward orbit relation \(x_{n+1}\in F(x_n)\) and follows from a coordinatewise connectedness argument tailored to that object.

## Limitations
The result is topological and qualitative. It does not quantify the geometry, dimension, or dynamical complexity of the resulting Cantor orbit set. It also does not characterize what happens when only some fibers are totally disconnected or nondegenerate. The literature search did not locate a later paper explicitly answering Question 3.18, but absence from indexed searches is not a proof that no independent solution exists.

## References
1. J. Amorocho, J. Camargo, S. Macías, *Orbit sets, transitivity, and sensitivity with upper semicontinuous maps*, arXiv:2507.12272v1, 16 July 2025. See Theorem 3.11, Theorem 3.16, and Question 3.18.
2. L. Alvin, S. Greenwood, J. P. Kelly, *Cantor sets as generalized inverse limits*, Fundamenta Mathematicae 266 (2024), 1--24. DOI: 10.4064/fm230609-22-3.
3. F. Capulín, F. R. Ruiz del Portal, M. Sánchez-Garrido, *The Cantor set and inverse limits of upper semi-continuous functions*, Boletín de la Sociedad Matemática Mexicana 30 (2024). DOI: 10.1007/s40590-024-00651-2.
