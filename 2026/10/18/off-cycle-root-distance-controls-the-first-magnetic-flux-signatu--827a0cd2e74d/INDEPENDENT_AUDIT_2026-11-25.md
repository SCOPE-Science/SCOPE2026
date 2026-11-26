# Independent mathematical audit

## correctness

PASS

Each bridge has zero net traversal and any walk of winding q≠0 crosses every bridge on the root-to-cycle route at least once in each direction. Conservation at cycle vertices gives the same signed net traversal q on each cycle edge. The length is therefore at least 2d+m|q| and has parity mq; any excess from cancelling traversals is even. Equality permits only the prescribed path out/back and |q| consecutive oriented circuits, giving T² C^|q| per orientation. Zero winding implies even length, so there is no lower-order imaginary amplitude to pair with a first-winding term. For m even the real amplitude first sees flux at L=m+2d and the constant amplitude doubles its coefficient on squaring. For m odd only even winding enters the real amplitude, first at K=2m+2d. The odd amplitude starts at L, and its square starts at 2L>K since d≥1. These facts give the signs from (−i)^L or (−i)^K, the factor of four from reversal and squaring, and the next even Taylor order as remainder. Gauge equivalence of −H with H at flux Φ+π for odd m proves exact half-periodicity, since −H conjugates the diagonal return amplitude. At the blind fluxes the contrast is identically zero; the orders refer to generic contrast. Replay: RESULT.md lines 17–34, or count bridge and cycle traversals as above. The frozen scripts/notes were inspected, not executed; the checker's printed 'lengths' summarize total vertex counts (3–13), not the cycle-length range (3–8), and its d=0 cases are separate controls.

## originality

PASS

Credit the prior rooted closed-walk framework, cycle-rooted parity effect, and on-cycle half-flux symmetry to Luppi. The distinct result is the weighted off-cycle delay and leading probability coefficient, especially the strictly earlier double-winding real contribution for odd cycles. The most relevant actual prior passages and indexed analogues do not supply it.

## value

PASS

An off-cycle local return measurement is a natural probe of where magnetic flux first becomes observable. The theorem gives its exact distance and weight dependence for arbitrary attached trees. In the odd case it identifies a genuine change in the leading interference mechanism relative to a cycle root, rather than just a shift of the on-cycle order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
