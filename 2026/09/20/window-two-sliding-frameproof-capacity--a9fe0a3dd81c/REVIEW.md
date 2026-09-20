# Review

## Correctness — PASS

The central local claim is necessary in the unrestricted-coalition model when \(n>q\): after a valid nonunique pirate mark with recipient set \(C\), every user in \(C\) must receive a globally unique mark in the next segment. If \(u\in C\) instead receives a nonunique next mark, then every mark in that two-segment pirate continuation has a recipient distinct from \(u\). More generally, every earlier valid mark is also nonunique. The coalition \(U\setminus\{u\}\) can therefore realize the pirate history while \(u\) matches two consecutive pirate marks. Because \(n>q\), a nonunique mark always exists in every future segment, so the history can be extended to an infinite valid broadcast. This contradicts sliding-window \(2\)-dynamic frameproofness.

Once \(s\) current recipients must be made unique, \(s\le q-1\): \(s>q\) is impossible, while \(s=q\) would consume every symbol uniquely despite \(n-q>0\) remaining users. Thus at most \(q-s\) symbols remain for the other \(n-s\) users. A next nonunique class has size at least
\[
\left\lceil\frac{n-s}{q-s}\right\rceil.
\]
If \(n>\max_{1\le s\le q-1}s(q-s+1)\), this lower bound is strictly larger than \(s\). Iteration forces a strictly increasing sequence of nonunique class sizes inside \(\{2,\ldots,q-1\}\), an impossibility. The maximum quadratic value is \(\lfloor(q+1)^2/4\rfloor\).

The construction is direct. For \(n=a(q-a+1)\), each segment contains \(a\) globally unique protected users and \(q-a\) ordinary classes of size \(a\). After a valid pirate mark, its size-\(a\) recipient class becomes the protected set. Hence a user matching the pirate in one segment receives a unique mark in the next and cannot match a valid next pirate mark. The \(a=1\) case has no valid nonunique marks and is trivially safe.

A finite exhaustive checker independently confirms the construction for every \(q\le6\), every \(1\le a<q\), and all nonunique pirate histories through six segments. This computation is supporting evidence only; the theorem is proved symbolically.

## Originality — PASS, to the best of our knowledge

The primary source inspected is Paterson's 2007 paper *Sliding-window dynamic frameproof codes*. It defines the model, gives restricted optimal constructions, and explicitly states that complete generality requires allowing the number of protected users to vary with the segment; it then asks whether such general schemes can support more users. Its general construction specializes at \(\beta=0,l=2\) to the lower-bound value \(\alpha(q-\alpha+1)\), while the published general unrestricted upper bound remains only \(q^l+O(q^{l-1})\).

Searches for exact and synonymous formulations included sliding-window dynamic frameproof codes, dynamic frameproof codes, window length two, \(2\)-dynamic frameproof terminology, variable protection parameters, and the candidate quadratic formula. No later work stating the unrestricted exact capacity was located. A 2026 MaRDI citation snapshot for Paterson's sliding-window paper lists five citing works. The later frameproof-specific item among them, Zhou and Zhou's *Wide-sense 2-frameproof codes*, studies a static descendant-set model rather than feedback-dependent sliding-window dynamics. The related 2007 *Sequential and dynamic frameproof codes* treats finite-window dynamic codes and sequential codes, not the continuously sliding feedback problem solved here.

No inaccessible source with a concrete theorem statement suggesting prior coverage was identified. Citation indexes and keyword searches can miss relevant work, so originality remains qualified as to the best of our knowledge.

## Value — PASS

Window length two is the shortest nontrivial sliding-window setting. The result gives its exact capacity for every alphabet size, resolves this special case of Paterson's general variable-protection question, and identifies a simple mechanism behind optimality: nonunique recipient classes must be converted completely into unique marks one segment later, while pigeonhole pressure forces a competing nonunique class among the remaining users.

The exact value
\[
\left\lfloor\frac{(q+1)^2}{4}\right\rfloor
\]
also shows that arbitrary history-dependent variation cannot improve on the balanced fixed-size construction in this case.

## Limitations

The theorem is confined to window length \(2\). The upper proof uses an unrestricted coalition, specifically \(U\setminus\{u\}\), and therefore does not establish the same bound for sliding-window \(2\)-dynamic \(c\)-frameproof codes when \(c\) is fixed and small. The finite exhaustive verification covers only small alphabets and bounded history length; it is not used as a substitute for the proof.

**Same-model review: passed. Independent audit: not yet performed.**
