# Self-review

## Correctness — PASS
A leaf attached to each bridge endpoint forces that endpoint to be dominated internally in every dominating set. All other vertices have only internal neighbors, so the restriction to every block must dominate that block; the converse is immediate. This produces an exact polynomial factorization for any joining tree. The 33-vertex input coefficients were independently verified by exact variable elimination at 34 distinct evaluation points; the source root at \(-4\) is simple and the two small-block factors do not vanish there. The order threshold follows from \(2a+3b\) representation.

## Originality — PASS (qualified)
The root of the 33-vertex seed is the known result of Alikhani–Griswold (2026), and the domination-irrelevant support bridge follows from Kotek et al. (2012); neither is claimed original. Full primary-source comparisons and semantic research searches did not locate the *combined connected every-order and arbitrary-multiplicity* construction. This is a limited synthesis of known tools, with residual historical priority uncertainty.

## Value — PASS
The primary 2026 paper explicitly asks for infinite families with root \(-4\). Disconnected unions answer a weak version trivially. The new statement gives connected examples at every order at least 35 and allows arbitrary exact root multiplicity, while retaining an explicit polynomial. This is a motivated structural consequence despite the elementary bridge argument.

## Closest literature and limits
Alikhani–Griswold, arXiv:2608.00109v1, Section 2 and open problem 3 (source graph, simple root); Kotek et al., Electron. J. Combin. 19(3) (2012), Theorems 3.10–3.11 (strictly more general irrelevant-edge framework). The present proof neither constructs other integer roots nor establishes minimal connected graph order. Priority searches are not an independence certificate.

Self-review: passed. Independent audit: not yet performed.
