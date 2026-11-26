# The efficiency defect of the printed Shapley formula for directed trust games

## Finding

Let \(\widehat\phi\) be the allocation given by the displayed formulas (8)–(9) in Corollary 3.3 of Ryzák and Kroupa, arXiv:2605.18157v1. For every directed trust game in their Definition 2.1, its shortfall from Shapley efficiency is exactly the total weight of the one-way arcs:

\[
v(N)-\sum_{i\in N}\widehat\phi_i
=\sum_{(i,j)\in E:\ (j,i)\notin E} a_{ij}.
\]

In particular, any positive-weight one-way arc forces the printed formula to fail. For the directed unit-weight cycle \(1\to2\to3\to1\) the printed vector is \((0,0,0)\), whereas the Shapley value is \((1,1,1)\). The defect is in the reciprocal-arc restriction in the printed internal term. The all-incident-arc formula for the internal contribution was already given by Bandhana, Kroupa, and García (2024, Proposition 3.6).

## Assumptions and scope

The graph is finite, simple, directed and loopless, with weights \(a_{ij}\in[0,1]\) on its arcs. A coalition receives the sum of its internal arc weights plus, for each coalition member, the minimum weight of incoming arcs from outside the coalition, with the empty minimum interpreted as zero. The Shapley value uses the ordinary uniform distribution over player orders. The claim compares a particular printed formula with the game's grand-coalition worth; it makes no assertion about formulas outside Corollary 3.3 of the specified version.

## Proof

Fix a target \(j\). Use the preprint's ordering of its \(m_j\) incoming arcs by nondecreasing weight, with ordered weights \(b_j(t)\) and \(b_j(0)=0\); put \(\Delta_j(t)=b_j(t)-b_j(t-1)\). From (8), the printed external term for target \(j\) itself is

\[
\sum_{t=1}^{m_j}\frac{\Delta_j(t)}{t}-\frac{b_j(m_j)}{m_j+1}.
\]

From (9), the external contribution associated with target \(j\) for its rank-\(r\) in-neighbor is

\[
\sum_{t=r+1}^{m_j}\frac{\Delta_j(t)}{t}-\frac{b_j(m_j)}{m_j+1}.
\]

No other player receives an external contribution associated with \(j\). For each \(t\), the term \(\Delta_j(t)/t\) appears once for the target and once for each of the \(t-1\) earlier in-neighbors. The last term appears \(m_j+1\) times. Hence summing over the players gives \(\sum_{t=1}^{m_j}\Delta_j(t)-b_j(m_j)=0\); this also holds when \(m_j=0\) and for any ordering of ties. The printed external terms thus sum to zero.

The first sum in (8) includes a pair only if both arcs exist. For each unordered reciprocal pair the term \((a_{ij}+a_{ji})/2\) appears for each of its endpoints. The sum of the resulting allocations is therefore the weight of all arcs having a reverse arc. Since \(v(N)\) is the weight of **all** arcs and \(v(\varnothing)=0\), this establishes the identity and its strict positivity if any one-way arc has positive weight.

The internal term can be corrected using the existing formula

\[
\phi_i(v_{\mathrm{int}})=\tfrac12\sum_{j:(i,j)\in E}a_{ij}+\tfrac12\sum_{j:(j,i)\in E}a_{ji}.
\]

Indeed, each arc is its weight times the unanimity game on its two endpoints; each endpoint is the later player in half the orders. This explains the difference between the internal expressions without making a novelty claim for the all-incident-arc identity.

For the unit directed triangle, every player contributes one external term from (8) of \(1-1/2\) and one from (9) of \(-1/2\). The printed first term vanishes, giving the zero vector. Evaluating the game directly gives \(v(\varnothing)=0\), \(v(\{i\})=1\), \(v(\{i,j\})=2\), and \(v(N)=3\). Thus each player's marginal worth is one in every position.

## Verification

The all-graph identity follows by counting the multiplicities in the displayed sums, with no numerical assumption. The accompanying `verify_trust_game.py` enumerates all eight coalitions and all six player orders exactly for the unit-cycle witness. It checks the coalition values and the internal and external Shapley allocations separately. Substitution into (8)–(9), as above, checks the printed allocation directly; the script does not parse the paper or check the all-graph identity.

## Relationship to prior work

Bandhana, Kroupa, and García define this trust game and explicitly give the all-incident-arc Shapley identity in Proposition 3.6. Ryzák and Kroupa reuse the definition and give an internal unanimity summand in Lemma 3.2, but the reciprocal restriction appears in Corollary 3.3. The result here identifies this inconsistency and quantifies the resulting failure of the printed full allocation. It does not claim novelty for Shapley efficiency, the underlying game, or the all-incident-arc formula.

## Limitations

This is a correction scoped to arXiv:2605.18157v1. A later revision may change the display. The efficiency diagnostic is silent when all one-way arcs have zero weight; efficiency alone is not a proof of an allocation formula. The literature comparison is bounded.

## References

1. David Ryzák and Tomáš Kroupa, “A Tractable Class of Cooperative Games Defined by Directed Networks: Unanimity Decomposition and Shapley Value,” arXiv:2605.18157v1, https://arxiv.org/pdf/2605.18157v1. Definition 2.1, Lemma 3.2 and Corollary 3.3, equations (8)–(9).
2. Arti Bandhana, Tomáš Kroupa, and Sebastián García, “Trust in Shapley: A Cooperative Quest for Global Trust in P2P Network,” AAMAS 2024, pp. 132–140, DOI:10.5555/3635637.3662860, https://www.ifaamas.org/Proceedings/aamas2024/pdfs/p132.pdf. Definition 3.1 and Proposition 3.6.
