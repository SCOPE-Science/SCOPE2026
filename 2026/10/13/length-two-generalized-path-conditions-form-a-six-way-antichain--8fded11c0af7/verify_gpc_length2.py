#!/usr/bin/env python3
from typing import Set, Tuple

Pair = Tuple[int, int]
WORDS = ["", "x", "b", "xx", "xb", "bx", "bb"]
WITNESSES = {
    "": ({0,1,2}, {(0,0),(0,2),(1,0),(1,1),(2,2)}),
    "b": ({0,1}, {(0,1),(1,0)}),
    "xx": ({0,1,2}, {(0,0),(0,1),(1,1)}),
    "xb": ({0,1,2}, {(0,0),(0,1),(0,2),(1,0),(1,1)}),
    "bx": ({0,1,2}, {(0,0),(0,1),(1,0),(1,1),(2,0)}),
    "bb": ({0,1,2}, {(0,1),(1,2),(2,0)}),
}
NONTRIVIAL = ["", "b", "xx", "xb", "bx", "bb"]

def converse(r: Set[Pair]) -> Set[Pair]:
    return {(v,u) for (u,v) in r}

def compose(s: Set[Pair], r: Set[Pair]) -> Set[Pair]:
    # s o r: first r, then s
    return {(a,c) for (a,b) in r for (b2,c) in s if b == b2}

def word_relation(wset: Set[int], r: Set[Pair], word: str) -> Set[Pair]:
    q = {(a,a) for a in wset}
    for letter in word:
        step = r if letter == "x" else converse(r)
        q = compose(step, q)
    return q

def holds(wset: Set[int], r: Set[Pair], word: str) -> bool:
    return word_relation(wset, r, word) <= r

def main() -> None:
    for chosen, (wset, r) in WITNESSES.items():
        truth = {word: holds(wset, r, word) for word in WORDS}
        assert truth["x"]
        assert truth[chosen]
        for other in NONTRIVIAL:
            if other != chosen:
                assert not truth[other], (chosen, other, truth)
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
