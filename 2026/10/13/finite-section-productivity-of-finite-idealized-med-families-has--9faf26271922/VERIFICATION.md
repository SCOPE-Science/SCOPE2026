---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof has two load-bearing parts.

First, for a finite \(\mathcal J\)-eventually-different family
\[
\mathcal E=\{f_0,\ldots,f_{k-1}\},
\]
the simultaneous pairwise-distinct set
\[
B=\bigcap_{i<j<k}\{n:f_i(n)\ne f_j(n)\}
\]
lies in \(\mathcal J^*\). Thus \(F(n)\ge k\) throughout a co-\(\mathcal J\) set.

For necessity, Lemma 4.23 of arXiv:2610.02350v1 converts FSP into \(\mathcal U^*\)-maximality for an ultrafilter \(\mathcal U\supseteq\mathcal J^*\). If \(\{n:F(n)=k\}\notin\mathcal U\), then on the \(\mathcal U\)-large set where the \(f_i\) are pairwise distinct and \(F(n)\ne k\), there is an extra coordinate value. Choosing that extra value pointwise produces a function with no \(\mathcal U\)-large equality set against any \(f_i\), a contradiction.

For sufficiency, if \(\{n:F(n)=k\}\in\mathcal J^+\), extend \(\mathcal J^*\) together with that fiber to an ultrafilter. On the large subset where the \(f_i\) are pairwise distinct, the \(k\) members exhaust every coordinate value. Any test function therefore agrees pointwise with one of them, and finite-union primeness of the ultrafilter makes one equality set large. Lemma 4.23 then gives FSP.

Second, a \(k\)-member \(\mathcal J\)-eventually-different family exists exactly when
\[
\{n:F(n)\ge k\}\in\mathcal J^*.
\]
Necessity follows from pairwise distinctness on \(B\). Sufficiency is witnessed by the \(k\) coordinate constants on that co-\(\mathcal J\) set, extended by \(0\) elsewhere.

Combining the two proves the exact existence criterion. The alternating \(\mathrm{Fin}\) example was checked symbolically: the exact \(k\)-fiber is infinite but not cofinite, while the at-least-\(k\) fiber is all of \(\omega\).

No finite computation, experimental enumeration, or unproved limit argument is used.
