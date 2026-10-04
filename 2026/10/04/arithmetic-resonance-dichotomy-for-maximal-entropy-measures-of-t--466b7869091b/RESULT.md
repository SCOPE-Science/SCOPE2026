# Arithmetic resonance dichotomy for maximal-entropy measures of three-dimensional flow time maps
## Finding
Let \(\varphi=\{\varphi^s\}_{s\in\mathbb R}\) be a \(C^\infty\) nonsingular flow with positive topological entropy on a compact three-dimensional manifold without boundary. By Zang's finiteness theorem, write the distinct ergodic measures of maximal entropy of the flow as \(\mu_1,\ldots,\mu_N\). Ledrappier--Lima--Sarig show that each measured flow \(\varphi\) on \(\mu_i\) is either Bernoulli or isomorphic to the product of a Bernoulli flow and a rotational flow. In the second case let \(c_i>0\) be the period of the rotational factor, and let \(I\) be the set of such indices. Define
\[
\mathcal R=\bigcup_{i\in I} c_i(\mathbb Q\setminus\{0\}).
\]
For every \(t\ne0\), every ergodic measure of maximal entropy of the time map \(T_t=\varphi^t\) is an ergodic \(T_t\)-component of one of the flow measures \(\mu_i\). Consequently:

* If \(t\notin\mathcal R\), then \(T_t\) has exactly \(N\) ergodic measures of maximal entropy, namely \(\mu_1,\ldots,\mu_N\).
* If \(t\in\mathcal R\), then \(T_t\) has continuum many ergodic measures of maximal entropy.

More explicitly, suppose \(\mu_i\) has rotational period \(c_i\) and \(t/c_i=p/q\in\mathbb Q\) in lowest terms with \(q\ge1\). In the product model, the rotational time map is rotation by \(p/q\). Haar measure decomposes into the uniform measures on its \(q\)-cycles, parametrized by a circle modulo the finite rotation subgroup. The \(\mu_i\)-ergodic components of \(T_t\) are exactly the products of these cycle measures with the Bernoulli time-\(t\) factor. There are continuum many of them, and every one has maximal entropy.

Thus the failure-of-finiteness times are exactly \(\mathcal R\). If \(I\) is empty, there are no exceptional nonzero times. Otherwise \(\mathcal R\) is countable and dense in \(\mathbb R\).

## Assumptions and scope
The flow is assumed \(C^\infty\), nonsingular, and defined on a compact three-dimensional manifold without boundary, with positive topological entropy. These are the hypotheses of the recent finiteness theorem used here. The statement concerns nonzero time maps. The periods \(c_i\) are measure-theoretic periods of the rotational factors in the Bernoulli-up-to-a-period classification; the theorem does not assert that they are topological periods of the ambient flow.

The conclusion is about ergodic measures of maximal entropy. It does not classify lower-entropy invariant measures, and it does not claim an effective procedure for computing the periods \(c_i\) from the vector field.

## Proof
Fix \(t>0\); the case \(t<0\) follows by replacing \(t\) by \(|t|\), since a homeomorphism and its inverse have the same invariant measures and entropies. Let \(\nu\) be an ergodic measure of maximal entropy for \(T_t=\varphi^t\). For \(0\le s<t\), put \(\nu_s=(\varphi^s)_*\nu\). Commutation of the flow maps shows that every \(\nu_s\) is \(T_t\)-invariant and ergodic, and \(\varphi^s\) gives a measure-theoretic conjugacy between \(\nu\) and \(\nu_s\), so their \(T_t\)-entropies agree.

Set
\[
\bar\nu=\frac1t\int_0^t (\varphi^s)_*\nu\,ds.
\]
Because \(\nu_{s+t}=\nu_s\), translating the integration interval proves that \(\bar\nu\) is invariant under the whole flow. Entropy is affine on the simplex of \(T_t\)-invariant measures, hence
\[
h_{\bar\nu}(T_t)=h_\nu(T_t)=h_{\mathrm{top}}(T_t).
\]
For a flow-invariant measure, entropy scales with time, and topological entropy does likewise, so
\[
h_{\bar\nu}(\varphi)=h_{\mathrm{top}}(\varphi).
\]
Thus \(\bar\nu\) is a flow measure of maximal entropy. It is also flow-ergodic: every flow-invariant measurable set is \(T_t\)-invariant, so its \(\nu\)-measure is zero or one, and the same is true after averaging. Zang's theorem therefore gives \(\bar\nu=\mu_i\) for some \(i\).

The probability distribution obtained by pushing normalized Lebesgue measure on \([0,t)\) through \(s\mapsto\nu_s\) is an ergodic decomposition of \(\mu_i\) for \(T_t\). Uniqueness of ergodic decomposition implies that almost every \(\nu_s\) is a canonical \(T_t\)-ergodic component of \(\mu_i\). Choosing one such \(s\) and translating back by \(\varphi^{-s}\), which commutes with \(T_t\) and preserves \(\mu_i\), shows that the original \(\nu\) is itself a \(T_t\)-ergodic component of \(\mu_i\).

It remains to compute those components. If \(\mu_i\) is Bernoulli for the flow, Ledrappier--Lima--Sarig recall that every nonzero time map is a Bernoulli automorphism, hence ergodic. If instead the measured flow is \(B^s\times R^s_{c_i}\), where \(B\) is Bernoulli and
\[
R^s_{c_i}(x)=x+s/c_i\pmod 1,
\]
then \(B^t\) is Bernoulli and therefore weakly mixing. When \(t/c_i\notin\mathbb Q\), the circle rotation is ergodic, so its product with the weakly mixing map \(B^t\) is ergodic. Thus \(\mu_i\) contributes exactly one ergodic \(T_t\)-MME.

When \(t/c_i=p/q\in\mathbb Q\) in lowest terms, the circle rotation has finite \(q\)-cycles. Haar measure decomposes into continuum many uniform \(q\)-cycle measures. The product of weakly mixing \(B^t\) with each ergodic \(q\)-cycle is ergodic. The rotation contributes zero entropy, so every such product has entropy equal to the entropy of \(\mu_i\) under \(T_t\), namely \(h_{\mathrm{top}}(T_t)\). Hence all are MMEs. This gives continuum many whenever any period is resonant. Since a compact metric space supports at most continuum many Borel probability measures, the cardinality is exactly continuum.

Taking the union over the finitely many \(\mu_i\) proves the dichotomy and the stated exceptional set.

## Verification
The proof is analytic and uses no numerical experiment. The critical inputs were checked directly against the cited sources: Zang proves finiteness of flow-ergodic MMEs and records the time-one ergodic-component averaging lemma; Ledrappier--Lima--Sarig define the rotational period, prove the Bernoulli-up-to-a-period structure, and state that every nonzero time map of a Bernoulli flow is Bernoulli. The standard time-map averaging argument was also compared with Fisher--Hasselblatt's treatment of maximal entropy for time-\(t\) maps.

Boundary cases were checked explicitly. If \(t/c_i\) is an integer, then \(q=1\) and the rotational time map is the identity, yielding continuum many point-fiber components. If \(I\) is empty, the exceptional set is empty. Negative \(t\) gives the same classification as \(|t|\).

## Relationship to prior work
Zang proves only that the continuous-time flow has finitely many ergodic MMEs. Ledrappier--Lima--Sarig prove that each such measured flow is Bernoulli up to a possible rotational period, but they do not state the global count of MMEs of arbitrary time maps for a flow with finitely many distinct flow MMEs. Fisher--Hasselblatt give the general averaging mechanism in the special situation of a unique weakly mixing flow MME and exhibit constant suspensions as the basic source of extra time-map MMEs. The present statement combines these ingredients with uniqueness of ergodic decomposition to identify every time-map MME and to give the exact arithmetic exceptional set and the finite-versus-continuum cardinality dichotomy.

A residual literature risk remains because the time-map argument is elementary once the Bernoulli-period decomposition is known; an equivalent finite-family arithmetic formulation may exist in unindexed lecture notes or folklore. The highly relevant Fisher--Hasselblatt section was located and its indexed theorem and constant-suspension example were compared; the uninspected remainder of that section remains a residual literature risk.

## Limitations
The theorem does not compute the periods \(c_i\), decide whether a given MME has a rotational factor from topological data alone, or extend Zang's nonsingular \(C^\infty\) hypotheses. It also does not address equilibrium states for nonzero potentials, where matching a time-map variational problem to the flow requires additional bookkeeping for the potential.

The claim is a structural consequence of the recent finiteness theorem, the earlier Bernoulli-up-to-period classification, and the time-map averaging/decomposition argument; it is not presented as a new construction of MMEs or as a strengthening of those input theorems themselves.

## References
1. Y. Zang, *Measures of maximal entropy for \(C^\infty\) three-dimensional flows*, arXiv:2503.21183. First public version: 2025-03-27.
2. F. Ledrappier, Y. Lima, O. Sarig, *Ergodic properties of equilibrium measures for smooth three dimensional flows*, Comment. Math. Helv. 91 (2016), 65--106; arXiv:1504.00048.
3. T. Fisher, B. Hasselblatt, *Hyperbolic Flows*, Zurich Lectures in Advanced Mathematics, EMS Press, 2019, Section 4.4.
