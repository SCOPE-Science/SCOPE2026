# Independent mathematical audit — SCOPE-20260920-a9fe0a3dd81c

Audited at: 2026-10-01T22:05:12.892464Z

Disposition: **passed**

## Correctness — PASS

With more users than alphabet symbols, every segment has a nonunique mark. If a pirate broadcasts a nonunique class of size \(s\), every recipient must receive a globally unique mark next; otherwise the coalition of all other users can extend the nonunique history and frame that recipient over two consecutive segments. Thus the remaining users occupy at most \(q-s\) symbols, so a next nonunique class has size at least \(\lceil(n-s)/(q-s)\rceil\). When \(n>s(q-s+1)\), this size is strictly larger than \(s\), producing an impossible strictly increasing sequence bounded by \(q-1\). The matching construction protects exactly the previous pirate class and attains \(a(q-a+1)\), whose integer maximum is \(\lfloor(q+1)^2/4\rfloor\).

### Correctness sources

- assigned RESULT.md
- Paterson, Sliding-window dynamic frameproof codes (2007)
- assigned finite construction artifact inventory

### Correctness risks

- The finite verifier through small alphabets is supplementary and not used as proof.
- The upper bound relies on unrestricted coalition size and does not extend as written to fixed small coalition bounds.

## Originality — PASS

Paterson's primary paper gives the fixed-parameter construction and proves optimality within that restricted family, then explicitly asks whether fully general schemes with history-dependent numbers of protected users can do better. Specializing the construction to window length two yields the lower bound in the assigned theorem, but the inspected paper does not give the unrestricted exact upper bound. Searches found no later source closing this window-two question.

### Equivalent formulations

No equivalent formulation was located under sequential/dynamic frameproof terminology.

Searches:
- Published-record semantic search: sliding-window dynamic frameproof code window length two exact capacity variable protection
- Literature search for dynamic frameproof, sliding-window frameproof, and window-two capacity

Evidence:
- The assigned theorem is the only exact unrestricted window-two hit.
- Later nearby coding results concern static or wide-sense frameproof codes, not the feedback-dependent sliding-window model.

### Broader coverage

The general framework is broader in window length, but it does not determine the exact unrestricted capacity at window length two.

Searches:
- Paterson 2007 full-text material
- Paterson 2007 sequential/dynamic companion paper
- later wide-sense frameproof literature

Evidence:
- Paterson treats general window length and a two-parameter restricted construction, with a broad asymptotic upper bound.
- The paper explicitly leaves fully general variable protection open.

### Exact database or table

The formula is proved by a new class-size growth argument rather than read from a catalog.

Searches:
- Published-record semantic database search for \(\lfloor(q+1)^2/4\rfloor\) in sliding-window dynamic frameproof coding

Evidence:
- No earlier exact capacity table or theorem was found.

### Claim versus prior implication

The audited protection lemma is the additional implication needed to close the open unrestricted case.

Searches:
- Compared the assigned lower construction and upper bound with Paterson's Construction 4.4 and restricted optimality discussion

Evidence:
- For window length two Paterson's fixed-\(\alpha\) construction gives \(\alpha(q-\alpha+1)\), matching the assigned lower bound.
- Paterson's restricted-family optimality does not imply optimality when the number protected may vary with history; the paper identifies exactly that gap.

### Sources inspected

- **Sliding-window dynamic frameproof codes** — https://doi.org/10.1007/s10623-006-9030-9
  - Trigger: Primary source defining the model and posing the variable-protection question.
  - Material read: Author-posted full-text material covering the model, Construction 4.4, the fixed-parameter optimality discussion, and the open-problem section.
  - Method: Primary full text.
  - Assessment: OPEN_PROBLEM_SOURCE
  - Evidence: The source supplies the matching fixed-parameter lower construction and explicitly leaves fully general variable protection unresolved.
- **Sequential and Dynamic Frameproof Codes** — https://doi.org/10.1007/s10623-006-9037-2
  - Trigger: Companion source on the broader dynamic/sequential frameproof setting.
  - Material read: Abstract and model-scope material.
  - Method: Primary publication metadata/abstract.
  - Assessment: BACKGROUND
  - Evidence: It gives constructions and bounds in the broader dynamic model but no exact unrestricted window-two formula.

### Checked sources

- https://doi.org/10.1007/s10623-006-9030-9
- https://doi.org/10.1007/s10623-006-9037-2
- https://doi.org/10.1007/s10623-020-00797-w
- published-record semantic search

### Residual risks

- Citation and keyword searches are not exhaustive, so an obscure later solution could exist.
- The theorem is specifically for unrestricted pirate coalitions.

## Value — PASS

The result exactly resolves the first nontrivial window length in an explicitly open unrestricted model, replacing a coarse quadratic-order bound by a sharp capacity and a simple structural obstruction. The result is naturally motivated by the source's open problem.

### Value sources

- Paterson 2007 primary full text

### Value risks

- The proof does not address fixed-coalition-size variants or longer windows.

## Limitations

- Window length two only.
- Unrestricted coalition size is essential to the upper-bound attack.
- The finite construction verifier is corroborative, not exhaustive evidence for the theorem.
- Originality is best-of-knowledge against incomplete citation coverage.
