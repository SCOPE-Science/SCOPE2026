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
# Reproduction and limitations

`verify.py` is a standalone Python 3 verifier without third-party dependencies. Run `python verify.py --check-certificate certificate.json` from a directory containing these two files, or provide the certificate's correct relative path. The program (i) constructs the twelve cube edges explicitly using binary triples; (ii) enumerates all degree-capped subgraphs; (iii) creates every matched pair from descending fixed pivots and checks that pairs are disjoint codimension-one incidences; (iv) builds all 7980 face-poset covers; (v) checks a directed topological order on all 1698 nonempty faces; and (vi) compares the exact recalculated face list, pair list, critical-cell list and topological order with the supplied certificate. The recorded output is `verification_output.txt`.

The four unmatched nonempty faces have mask encodings 888, 1235, 1421 and 2048, corresponding respectively to three critical cells of dimension five and one of dimension zero. By discrete Morse theory their CW model has no cells in intermediate dimensions, so it is the asserted wedge without an uncomputed attaching differential. The separate mod-two chain computation obtains unreduced Betti numbers (1,0,0,0,0,3,0,0) in dimensions zero through seven and corroborates the Euler characteristic, but is not treated as proof of an integral homotopy type. Numerical verification is exhaustive **only** for this stated twelve-edge graph. Independent mathematical audit has not been performed.
