# Independent mathematical audit

## correctness

PASS

Prefix language is factorial. Allowed morphism count is exactly 3 sum_{L=2}^5 (L-1)3^L=3834 with both images length 4..7. Appending a letter can create only a new square suffix or a new suffix equal to either formula-fragment image whose other fragment appears in the word. Therefore exact suffix-pruning traverses every admissible word at each depth. Independent fresh Python enumerator reproduced all 47 survivor counts, ending 36,30,24,18,0 at lengths 42..46, and directly checked each of the 18 length-45 words against all 3834 morphisms and square condition; orbit under six letter permutations and reversal has sizes 6,12. None at 46 excludes all longer words. This does NOT bound unrestricted formula-avoiding words.

## originality

PASS

Ochem & Rosenfeld, arXiv:1706.03233 v2 p9/section6 explicitly state only absence of an infinite square-free ternary word under exactly the restrictions |h(A)|=1, |h(B)|+|h(C)|<=5. Their proof states a computer check without a finite maximum, enumeration or orbit profile. Here 45 and all 18 extremizers are separately computed; an archived unindexed input or code could contain these counts, retained as risk. No whole-paper absence assertion beyond inspected primary section.

## value

PASS

The exact maximum length and equality classes sharpen a natural bounded computational certificate underlying an established 4-avoidability theorem; the cutoff identifies a usable finite search depth and all extremal counterexamples, not an arbitrary slice or known count recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
