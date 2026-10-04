#!/usr/bin/env python3
left = [
    ["x", "y", "z"],
    ["z", "x", "y"],
    ["y", "z", "x"],
]
reflected = [list(reversed(row)) for row in left]
assert reflected == [["z","y","x"],["y","x","z"],["x","z","y"]]
assert [reflected[0][2], reflected[1][1], reflected[2][0]] == ["x","x","x"]
S = 2**9 // 2
G = 8 * S
assert S == 256
assert G == 2048
assert S // 64 == 4
assert G // 128 == 16
print("VERIFY_OK")
