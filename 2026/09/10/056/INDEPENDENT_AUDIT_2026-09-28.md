# Independent Audit — 2026/09/10/056

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `6e797fede6d6e0adfee6981ad4237e60d070ff9c`  
**Disposition:** **PASSED**

## Correctness

**Verdict:** PASS

The q=11 counterexample is exact. Independent mod-11 matrix arithmetic gives det(X)=det(Y)=det(Z)=1, [X,Y]=[[10,5],[0,10]], [X,Y]^2=[[1,1],[0,1]]=U, and Z^3=10I=-I. Hence w=[X,Y]^2 Z^3=-U, which represents the same PSL(2,11) element as U because ±I are identified. Since 11≡3 mod 4 and 11>=11, this single witness refutes the universal omission statement exactly. The representative U is nontrivial unipotent, and any class-splitting nuance is irrelevant because the witness hits the specified representative itself.

## Originality

**Verdict:** PASS

Targeted searches for the exact word [x,y]^2 z^3, PSL(2,11), and an unipotent hit found no prior statement or table containing this witness. The closest literature treats different non-surjective words, Engel words, or asymptotic/product Waring phenomena and does not imply this small-group fibre value. The exact counterexample therefore appears original within the searched literature.

## Scientific value

**Verdict:** PASS

Although narrow, the result decisively falsifies a motivated universal claim at the first admissible field size. An explicit short witness is reusable and prevents further work on a false all-q omission conjecture. The record appropriately does not overclaim full surjectivity at q=11 or behavior for larger q.

## Limitations

- Only the universal omission claim is decided; the full image/fibre distribution of the word on PSL(2,11) and larger q remains open.
- Priority checking was targeted rather than exhaustive; an obscure unpublished enumeration cannot be ruled out solely by search.

## Literature and evidence

- [Biswas–Saha, On non-surjective word maps on PSL_2(F_q)](https://arxiv.org/abs/2012.01408): Nearest prior work constructs different non-surjective two-variable words; it does not cover [x,y]^2 z^3 or the q=11 unipotent witness.
- [Jambor–Liebeck–O’Brien, Some word maps that are non-surjective on infinitely many finite simple groups](https://arxiv.org/abs/1205.1952): Provides broader non-surjective word-map context but not this word or fibre.

- Independent 2×2 matrix arithmetic mod 11 verified the witness exactly.
- Exact-word and exact-group searches found only different-word prior work.
- Repository research files were read at the assigned tree; no GitHub writes were made.

Repository evidence was read from `SCOPE-Science/SCOPE2026`. No repository writes were made by this audit.
