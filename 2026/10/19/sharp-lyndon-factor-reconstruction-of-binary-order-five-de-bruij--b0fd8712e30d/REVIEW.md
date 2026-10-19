# Scientific review

**Correctness — PASS.** The finite domain is complete because every directed Eulerian circuit corresponds to one local incoming/outgoing pairing at each graph vertex, with a single edge cycle. An unrelated depth-first enumeration agrees on all \(2048\) canonical representatives. Two mathematically equivalent but separately implemented Lyndon predicates produce the same full profiles. The exhaustive table and checker establish exactly one collision at cutoff \(18\) and none at cutoff \(19\). There is no inference from a random sample to an infinite assertion.

**Originality — PASS relative to inspected and retrieved literature, with residual priority risk.** Saari (2012) develops factor-count bounds and recurrent-word results and cites the Lyndon/de Bruijn construction; Goc–Saari–Shallit (2012) studies Lyndon factors in automatic sequences. Glen–Simpson–Smyth (2017) gives unrestricted finite-word extremal/mean counts, not de Bruijn reconstruction. Daykin et al. (2018) treats positional Lyndon arrays; a full positional array is not the vector of aggregate distinct Lyndon factor counts here. Targeted published-result searches and a comparison with accessible existing claims found no equivalent order-five, cutoff-\(19\) result. A potentially relevant author-version download of the 2018 paper was inaccessible, so only its published abstract was assessed; earlier unindexed enumerations also remain possible.

**Mathematical value — PASS.** Every binary order-five de Bruijn cycle has identical ordinary factor complexity at all lengths. Nevertheless, just fourteen Lyndon-factor counts at lengths \(6\) through \(19\) distinguish every cycle, with a uniquely witnessed sharp boundary. This supplies a natural complete reconstruction benchmark connecting Lyndon-factor complexity and universal cycles; it is not just an arbitrary moment table.

**Scope and limitations.** The theorem is restricted to order five over an ordered binary alphabet, modulo rotation, and uses exact finite computation rather than a uniform all-order argument. Historical priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
