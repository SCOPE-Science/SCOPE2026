---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The exact final claim is a finite complete classification, not a partial enumeration. Height four means four vertices in a longest chain; in a rooted poset the sole depth-3 point is the root. Nonroot depth-1 points immediately cover distinct subsets of the 3 maxima of cardinality at least 2, yielding at most one for each of four sets ab/ac/bc/abc and hence Q_T. Nonroot depth-2 point covers an antichain of at least 2 points containing at least one depth-1 vertex; conversely any such antichain defines a unique depth-2 point without duplicate cover sets. The selected nonempty family U cannot be the singleton of all minimal points of Q_T, which otherwise leaves the root with only one cover. All other U give root at least 2 covers, and its cover set includes a depth-2 point, preventing coincidence. Induction on depth reconstructs every source poset uniquely. With labelled maxima, sums of (2^|A(T)|-2) give 16718; S3 relabeling exhausts all isomorphisms because cover sets force every lower vertex, with fixed counts identity 16718, transpositions 1070 each, 3-cycles 68 each, yielding (16718+3*1070+2*68)/6=3344. The source correctly invokes the published equivalence of finite regular Esakia duals and cover-set regular posets (Grilletti–Quadrellaro, Theorem 4.7), and 3 maxima give 8 double-negation-fixed elements (Corollary 3.5). An independently written exact Python program, not executing the repository verifier, enumerated ALL 16718 normal-form choices; reconstructed closure and cover edges for each, tested least root, 3 maxima, unique nonmaximal successor sets of size >=2, height 4, canonical S3 orbits and fixed counts, matching 3344, and size range 7..22. The independent enumeration corroborates the finite census; the conceptual exhaustive-normal-form proof establishes completeness.

## originality

PASS

Grilletti–Quadrellaro (arXiv:2303.11246, Algebra Universalis 85:5) provides Theorem 4.7, the necessary-and-sufficient finite regular-cover criterion, and Corollary 3.5 relating Boolean fixed elements to maxima. Its Section 5 gives special infinite families with three maxima, while Section 7 expressly asks for classification of finite regular posets by depth/maxima; the journal text examined does not provide this complete height-four three-maxima 3344-orbit census or its S3-equivariant antichain normal form. Fresh queries through Resultary, published SCOPE records, and public literature for the exact pair of restrictions, alternative rooted-frame terminology, and integers 3344/16718 found no covering published count; nonmatching hits are not novelty proof. The result is therefore best-of-knowledge original as the exact bounded complete classification, while crediting the crucial prior duality and membership theorem.

## value

PASS

The original primary work specifically asks for a classification of finite regular Esakia posets by combinatorial dimensions, including depth and number of maximal elements. Three maxima constitute an 8-element regular Boolean core; height four is a natural first nontrivial case with interacting two-level antichain choices below that core. The reversible, S3-equivariant normal form is mathematically useful independently of the integer: it parametrizes representatives and bounds size (7 through 22 vertices). The complete 3344-class result resolves that meaningful bounded problem and constrains finite regularly generated, subdirectly irreducible Heyting-algebra examples. The result does not claim distinct logics, full algebra sizes, a classification for other depths or arbitrary numbers of maxima, and does not rely on novelty or the verifier alone to establish value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
