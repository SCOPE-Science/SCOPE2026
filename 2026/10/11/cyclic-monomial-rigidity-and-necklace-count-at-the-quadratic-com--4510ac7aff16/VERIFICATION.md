---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For coprime p,q>=1, c>0, n=p+q and invertible T, decompose A=S+K into commuting semisimple/nilpotent Jordan parts. On each difference-eigenvalue space of ad_S, the nilpotent ad_K perturbation of f(z)=(z-pc)(z+qc) has invertible f unless the eigenvalue is a root, forcing each nonzero T entry to connect eigenvalues differing by pc or -qc. Invertibility supplies a nonzero permutation determinant term. Every cycle has q t positive edges and p t negative edges for integer t>=1; hence length n t; at n indices the permutation must be one length-n cycle, forcing n pairwise distinct eigenvalues (no proper zero-increment segment). Then K=0 because it commutes with simple-spectrum S and is nilpotent. The cycle partial sums are distinct mod n since p is coprime to n; the two possible outgoing targets from any source have the same residue and only one vertex of that residue occurs, so T has exactly the cycle nonzero support. Conversely every balanced binary word and nonzero weights realizes a solution. Every balanced word is primitive since gcd(q,n)=1. Unique intrinsic successor recovers the word up to rotation from its spectral set, so the count is binom(n,q)/n (translation only, no scaling). The monomial cycle product W gives T^n=WI=(-1)^(n-1)det(T)I; D=ad_A(T) multiplies q weights by pc and p by -qc, giving det(D)=(-1)^p p^q q^p c^n det(T) and D^n=(-1)^(n-1+p)p^q q^p c^n det(T)I. Checked small n=2 and degenerate p=1 or q=1 boundaries. Independent exact combinatorial enumeration for all 23 coprime ordered pairs 1<=p,q<=6 confirmed primitive cycles, unique successor, distinct translation-normalized spectra, and necklace counts; finite checks not used as proof of universal quantifiers.

## originality

PASS

The closest primary antecedent, Stanković arXiv:2608.29574v1, was now inspected in its 17-page PDF rather than merely its abstract. Theorem 6.1 and Corollary 6.4 prove the nilpotency/existence dimension threshold; Proposition 6.2 constructs a cyclic invertible pair from ANY balanced q-plus/p-minus sequence. They do NOT state that EVERY invertible threshold pair is simultaneously similar to a cyclic monomial pair, that A must have simple spectrum, that the allowed support is unique, or that spectra modulo translation are classified injectively by primitive necklaces. Theorem 8.1 remains a nilpotency-regime classification. This distinction is genuine necessity versus existence, not a change of names. The new determinant cycle-cover / simple-spectrum / forced-support argument supplies necessity. Three new Resultary semantic searches return the assessed record itself as the sole direct match, with other hits involving different mathematical objects. Hence best-of-knowledge independent originality PASS for full rigidity and spectral-shape enumeration, not for the dimension threshold or individual existence constructions.

## value

PASS

At a sharp n=p+q resonance threshold where prior work supplies existence of invertible cyclic examples, the exhaustive equality-case question is natural and consequential: every invertible extremizer has simple A-spectrum and one weighted cyclic support, with an exact global classification of permitted spectral shapes and scalar-power rigidity of T and ad_A(T). The converse excludes nonsemisimple and multi-cycle possibilities not decided by a mere example or threshold obstruction. The primitive-necklace count rests on the nontrivial matrix-to-word bijection rather than a table lookup. This is a structural classification, not a new threshold theorem or mere finite enumeration; no theorem about dimensions n>p+q, singular T, or full continuous weight moduli is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
