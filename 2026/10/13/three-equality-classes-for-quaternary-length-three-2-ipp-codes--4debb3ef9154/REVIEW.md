# Review of Three equality classes for quaternary length-three \(2\)-IPP codes

## Correctness
PASS. The source proof gives the exact maximum \(F(3,4)=5\): after selecting a partial-order-minimal maximum graph, the \(q=4\) case can only be type III or IV; the source's bounds give at most five vertices in either case and it supplies five-vertex witnesses. The embedded verifier then independently checks the complete equality layer directly from the descendant/intersection definition. It examines all \(595{,}665\) normalized candidates containing `000`, obtains exactly \(4{,}320\) valid codes, finds exactly three canonical equivalence classes, and rechecks the resulting incidence and orbit-stabilizer arithmetic.

## Originality
PASS. The closest primary full text proves the scalar optimum and deliberately restricts its structural classification to a selected partial-order-minimal maximum graph. It displays the type-III and type-IV minimal shapes for \(q=4\), but does not enumerate all maximum codes. The complete census finds a third equality orbit with a three-color 2-clique binding plus an isolated codeword; that graph is maximum but nonminimal for the source's ordering. Exact-number, orbit, graph-shape, and alias searches found no statement implying the three classes, \(55{,}296\) labeled maxima, or stabilizers \(4,6,4\). The closest indexed tracing result is for the strictly stronger \(2\)-traceability property and cannot cover this equality layer.

## Value
PASS. The result is a complete classification at a named exact benchmark, rather than a new computation of the already-known optimum. Its structural point is that the classical partial-order reduction is sufficient for the extremal cardinality but not for an equality-case census: one entire nonminimal orbit is hidden by that reduction. The exact orbit counts and stabilizers also provide a compact benchmark for equivalence testing of small identifiable-parent codes.

## Closest literature and limitations
The decisive source comparison is Tô--Safavi-Naini's full length-three maximum-code article, especially its equivalence definition, the explicit selection of a partial-order-minimal maximum graph, the structural theorems, Theorem 34, and Figure 35. The foundational 1998 article establishes the object and historical bounds but was not used as a whole-document negative originality source. Residual risk is an obscure or poorly indexed historical enumeration.

Self-review: passed. Independent audit: not yet performed.
